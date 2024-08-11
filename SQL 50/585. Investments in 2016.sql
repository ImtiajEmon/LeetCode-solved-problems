# Write your MySQL query statement below

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM
    (SELECT *,
    COUNT(*) OVER(PARTITION BY tiv_2015) AS cnt1,
    COUNT(*) OVER(PARTITION BY lat, lon) AS cnt2
    FROM Insurance) t
WHERE cnt1 > 1 AND  cnt2 = 1;
