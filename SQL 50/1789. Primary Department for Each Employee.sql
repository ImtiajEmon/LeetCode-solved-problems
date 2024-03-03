# Write your MySQL query statement below
WITH cte AS(
    SELECT employee_id, CASE
    WHEN COUNT(*) = 1 THEN department_id
    WHEN COUNT(*) > 1 THEN SUM((primary_flag = 'Y') * department_id)
    END AS department_id
    FROM Employee
    GROUP BY employee_id
)

SELECT *
FROM cte
WHERE department_id != 0;
