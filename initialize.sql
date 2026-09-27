DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    join_date DATETIME
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(200),
    content TEXT,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, name, email, join_date)
VALUES (1, 'Emma Johnson', 'emma@example.com', '2026-01-10 10:00:00');

INSERT INTO users (user_id, name, email, join_date)
VALUES (2, 'Liam Smith', 'liam@example.com', '2026-01-15 11:30:00');

INSERT INTO users (user_id, name, email, join_date)
VALUES (3, 'Olivia Brown', 'olivia@example.com', '2026-02-01 09:15:00');

INSERT INTO users (user_id, name, email, join_date)
VALUES (4, 'Noah Davis', 'noah@example.com', '2026-02-10 14:00:00');

INSERT INTO users (user_id, name, email, join_date)
VALUES (5, 'Ava Wilson', 'ava@example.com', '2026-03-05 16:45:00');

INSERT INTO users (user_id, name, email, join_date)
VALUES (6, 'Ethan Miller', 'ethan@example.com', '2026-03-12 12:00:00');

INSERT INTO users (user_id, name, email, join_date)
VALUES (7, 'Mia Moore', 'mia@example.com', '2026-04-01 08:30:00');

INSERT INTO users (user_id, name, email, join_date)
VALUES (8, 'Lucas Taylor', 'lucas@example.com', '2026-04-18 13:20:00');

INSERT INTO users (user_id, name, email, join_date)
VALUES (9, 'Sophia Anderson', 'sophia@example.com', '2026-05-02 15:10:00');

INSERT INTO users (user_id, name, email, join_date)
VALUES (10, 'James Thomas', 'james@example.com', '2026-05-20 17:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (1, 1, 'First Post', 'This is my first post.', '2026-06-01 10:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (2, 2, 'SQL Practice', 'I am learning SQL today.', '2026-06-02 11:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (3, 3, 'Data Science', 'Data science is interesting.', '2026-06-03 12:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (4, 4, 'Python', 'Python is useful for data analysis.', '2026-06-04 13:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (5, 5, 'Databases', 'Today I learned about databases.', '2026-06-05 14:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (6, 1, 'Second Post', 'Here is another post.', '2026-06-06 15:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (7, 2, 'MySQL', 'MySQL stores relational data.', '2026-06-07 16:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (8, 3, 'Pandas', 'Pandas makes working with data easier.', '2026-06-08 17:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (9, 4, 'Learning', 'I enjoy learning new programming skills.', '2026-06-09 18:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (10, 5, 'Final Post', 'This is the final sample post.', '2026-06-10 19:00:00');