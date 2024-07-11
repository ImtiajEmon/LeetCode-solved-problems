SELECT t1.id
FROM Weather t1 JOIN Weather t2
ON DATE_SUB(t1.recordDate, INTERVAL 1 DAY) = t2.recordDate
WHERE t1.temperature > t2.temperature;
