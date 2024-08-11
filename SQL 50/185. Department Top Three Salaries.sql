# Write your MySQL query statement below

SELECT Department, Employee, Salary
FROM
    (SELECT t2.name AS Department, t1.name AS Employee, Salary,
    DENSE_RANK() OVER(PARTITION BY t2.name ORDER BY Salary DESC) AS serial
    FROM Employee t1
    JOIN Department t2
    ON t1.departmentId = t2.id) t
WHERE serial <= 3;
