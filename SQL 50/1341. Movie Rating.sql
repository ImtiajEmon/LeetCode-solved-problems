# Write your MySQL query statement below
WITH user_name AS(
    SELECT name, COUNT(*) AS rating_count
    FROM MovieRating t1 JOIN Users t2
    ON t1.user_id = t2.user_id
    GROUP BY t1.user_id
    ORDER BY rating_count DESC, name ASC
    LIMIT 1
),

movie_name AS(
    SELECT t2.title, AVG(rating) AS avg_rating
    FROM MovieRating t1 JOIN Movies t2
    ON t1.movie_id = t2.movie_id
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
    -- WHERE MONTHNAME(created_at) = 'February' AND YEAR(created_at) = 2020
    GROUP BY t2.title
    ORDER BY avg_rating DESC, title ASC
    LIMIT 1
)

SELECT name AS results
FROM user_name
UNION ALL
SELECT title AS results
FROM movie_name;
