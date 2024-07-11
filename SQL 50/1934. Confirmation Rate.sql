WITH joined_table AS(
    SELECT t1.user_id, t2.action,
    CASE WHEN t2.action = 'confirmed' THEN 1
    ELSE 0 END AS scaled_action
    FROM Signups t1 LEFT JOIN Confirmations t2
    ON t1.user_id = t2.user_id
)


SELECT user_id, ROUND(SUM(scaled_action) / COUNT(*), 2) AS confirmation_rate
FROM joined_table
GROUP BY user_id;
