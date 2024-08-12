# Write your MySQL query statement below

-- Solution - 1
-- DELETE p2
-- FROM Person p1 JOIN Person p2
-- ON p1.email = p2.email AND p1.id < p2.id

-- Solution - 2
DELETE FROM Person
WHERE id IN (SELECT id FROM
                        (SELECT *,
                        ROW_NUMBER() OVER(PARTITION BY email ORDER BY id) AS serial
                        FROM Person) t
                        WHERE serial > 1)
