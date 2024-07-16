# Write your MySQL query statement below

-- Solution - 1
-- WITH cte1 AS(
--     SELECT requester_id AS id1, COUNT(*) AS f_count1
--     FROM RequestAccepted
--     GROUP BY requester_id
-- ),
-- cte2 AS(
--     SELECT accepter_id AS id2, COUNT(*) AS f_count2
--     FROM RequestAccepted
--     GROUP BY accepter_id
-- ),

-- cte3 AS(
--     SELECT *
--     FROM cte1 LEFT JOIN  cte2
--     ON cte1.id1 = cte2.id2

--     UNION

--     SELECT *
--     FROM cte1 RIGHT JOIN  cte2
--     ON cte1.id1 = cte2.id2
-- )

-- SELECT
-- CASE
--     WHEN id1 IS NOT NULL THEN id1
--     ELSE id2
--     END AS id,
-- (CASE WHEN f_count1 IS NULL 
--     THEN 0 ELSE f_count1 END + 
-- CASE WHEN f_count2 IS NULL 
--     THEN 0 ELSE f_count2 END)
-- AS num
-- FROM cte3
-- ORDER BY num DESC
-- LIMIT 1;


-- Solution - 2
WITH cte AS(
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
)

SELECT id, COUNT(*) AS num
FROM cte
GROUP BY id
ORDER BY num DESC
LIMIT 1;
