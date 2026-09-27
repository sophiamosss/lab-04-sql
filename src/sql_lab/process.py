import logging
import os

import mysql.connector
import pandas as pd


# Set up logging so we can see what the script is doing.
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


# Read database information from environment variables.
DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")


def read_data(filename):
    """Read a CSV file and return it as a pandas DataFrame."""
    logging.info("Reading data from %s", filename)

    data = pd.read_csv(filename)

    logging.info("Data successfully loaded.")
    return data


def clean_data(data):
    """Remove rows containing missing values and return the cleaned DataFrame."""
    logging.info("Cleaning data.")

    # Remove any row that contains a missing value.
    cleaned_data = data.dropna()

    logging.info("Rows before cleaning: %d", len(data))
    logging.info("Rows after cleaning: %d", len(cleaned_data))

    return cleaned_data


def load_data(data, table):
    """Create the mock table if needed and upload the DataFrame to MySQL."""
    logging.info("Connecting to MySQL.")

    connection = None
    cursor = None

    try:
        # Connect to our MySQL database.
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
            port=3306,
        )

        cursor = connection.cursor()

        # Create the table that will hold our cleaned Mockaroo data.
        create_table_query = """
        CREATE TABLE IF NOT EXISTS mock (
            id BIGINT PRIMARY KEY,
            `group` VARCHAR(255),
            first_name VARCHAR(255),
            age BIGINT,
            email VARCHAR(255),
            city VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)

        # Clear old rows so rerunning this script does not duplicate data.
        cursor.execute("DELETE FROM mock")

        # Use placeholders instead of inserting values directly into SQL.
        insert_query = """
        INSERT INTO mock
            (id, `group`, first_name, age, email, city)
        VALUES
            (%s, %s, %s, %s, %s, %s)
        """

        # Insert each cleaned DataFrame row into MySQL.
        for row in data.itertuples(index=False):
            values = (
                int(row.id),
                row.group,
                row.first_name,
                int(row.age),
                row.email,
                row.city,
            )

            cursor.execute(insert_query, values)

        # Save all of our inserts.
        connection.commit()

        logging.info(
            "Successfully uploaded %d rows to table %s.",
            len(data),
            table,
        )

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)

    finally:
        # Close the cursor and database connection when finished.
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()

        logging.info("Database connection closed.")


def main():
    """Run the complete CSV cleaning and database upload process."""
    data = read_data("MOCK_DATA.csv")
    cleaned_data = clean_data(data)
    load_data(cleaned_data, "mock")


if __name__ == "__main__":
    main()