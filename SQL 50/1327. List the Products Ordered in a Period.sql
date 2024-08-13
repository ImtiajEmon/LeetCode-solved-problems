# Write your MySQL query statement below

SELECT product_name, SUM(unit) AS unit
FROM Products t1 JOIN Orders t2
ON t1.product_id = t2.product_id
WHERE MONTH(t2.order_date) = 2 AND YEAR(t2.order_date) = 2020
GROUP BY product_name
HAVING unit >= 100;
