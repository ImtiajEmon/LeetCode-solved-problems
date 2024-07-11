WITH cte AS(
    SELECT t1.*, t2.num AS num1
    FROM Logs t1 JOIN Logs t2
    ON t1.id + 1 = t2.id
),

cte1 AS(
    SELECT t1.*, t2.num AS num2
    FROM cte t1 JOIN Logs t2
    ON t1.id + 2 = t2.id
)

SELECT DISTINCT(num) AS ConsecutiveNums
FROM cte1
WHERE num = num1 AND num = num2;
