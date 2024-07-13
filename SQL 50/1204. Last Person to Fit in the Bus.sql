# Write your MySQL query statement below

SELECT DISTINCT(LAST_VALUE(person_name) OVER()) AS person_name

FROM (
    SELECT *,
    SUM(weight) OVER(ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_weight
    FROM Queue
) t
WHERE cumulative_weight <= 1000;
