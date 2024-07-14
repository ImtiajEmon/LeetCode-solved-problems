# Write your MySQL query statement below

WITH cte AS(
    SELECT visited_on, SUM(amount) AS amount,
    RANK() OVER(ORDER BY visited_on) AS serial
    FROM Customer
    GROUP BY visited_on
),

cte2 AS(
    SELECT *,
    SUM(amount) OVER(ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS cumulative_amount,
    ROUND(AVG(amount) OVER(ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM cte
)

SELECT visited_on, cumulative_amount AS amount, average_amount
FROM cte2
WHERE serial > 6;
