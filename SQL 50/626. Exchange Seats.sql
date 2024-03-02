WITH cte AS(
    SELECT *, LEAD(id) OVER(ORDER BY id) AS next, LAG(id) OVER(ORDER BY id) AS Prev
    FROM Seat
)

SELECT CASE
WHEN (id % 2 = 1 AND next IS NOT NULL) THEN next
WHEN (id % 2 = 1 AND next IS NULL) THEN id
ELSE prev
END AS id, student
FROM cte
ORDER BY id;
