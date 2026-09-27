import logging
import os

import mysql.connector


# Set up logging so we can see what the program is doing.
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


# Read database connection information from environment variables.
DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")


def get_data_by_group(value):
    """Return all rows from mock where the group column equals value."""
    logging.info("Getting rows where group equals %s.", value)

    connection = None
    cursor = None

    try:
        # Connect to the MySQL database.
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
            port=3306,
        )

        cursor = connection.cursor()

        # GROUP is a reserved MySQL word, so the column uses backticks.
        # %s is a safe placeholder for the value we are searching for.
        query = """
        SELECT *
        FROM mock
        WHERE `group` = %s
        """

        cursor.execute(query, (value,))
        results = cursor.fetchall()

        logging.info("Found %d matching rows.", len(results))
        return results

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        return []

    finally:
        # Always close the database connection when finished.
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


def plot_counts(groupby):
    """Count and return rows grouped by the specified column."""
    logging.info("Counting rows grouped by %s.", groupby)

    connection = None
    cursor = None

    try:
        # Connect to the MySQL database.
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
            port=3306,
        )

        cursor = connection.cursor()

        # Only allow known column names because SQL identifiers
        # cannot be safely passed using a %s value placeholder.
        allowed_columns = {
            "id": "id",
            "group": "`group`",
            "first_name": "first_name",
            "age": "age",
            "email": "email",
            "city": "city",
        }

        if groupby not in allowed_columns:
            raise ValueError("Invalid column name.")

        column = allowed_columns[groupby]

        # The column comes only from our safe allowlist above.
        query = (
            f"SELECT {column}, COUNT(*) "
            f"FROM mock "
            f"GROUP BY {column} "
            f"ORDER BY COUNT(*) DESC"
        )

        cursor.execute(query)
        results = cursor.fetchall()

        logging.info("Count query completed successfully.")
        return results

    except (mysql.connector.Error, ValueError) as error:
        logging.error("Query error: %s", error)
        return []

    finally:
        # Always close the database connection when finished.
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


def main():
    """Run example queries against the mock table."""
    # Demonstrate the parameterized group filter.
    group_results = get_data_by_group("Group A")

    print("\nFirst 5 rows from Group A:")
    for row in group_results[:5]:
        print(row)

    # Demonstrate counts grouped by the group column.
    counts = plot_counts("group")

    print("\nCounts by group:")
    for group, count in counts:
        print(group, count)


if __name__ == "__main__":
    main()