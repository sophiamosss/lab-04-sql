SELECT
    users.name,
    posts.title,
    posts.content,
    posts.created_at
FROM users
JOIN posts
    ON users.user_id = posts.user_id
WHERE posts.user_id <= 3;