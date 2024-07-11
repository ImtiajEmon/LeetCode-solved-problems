-- Solution - 1

WITH date_rank AS(
    SELECT *,
    RANK() OVER(PARTITION BY player_id ORDER BY event_date) AS date_rank
    FROM Activity
),

next_day AS(
    SELECT player_id, 
    DATE_ADD(event_date, INTERVAL 1 DAY) AS next_day
    FROM date_rank
    WHERE date_rank = 1
),

players_on_next_day AS(
    SELECT t1.player_id
    FROM Activity t1 JOIN next_day t2
    ON t1.player_id = t2.player_id
    WHERE t1.event_date = t2.next_day
    GROUP BY t1.player_id
)

SELECT ROUND(COUNT(*) / (SELECT COUNT(DISTINCT(player_id)) FROM Activity), 2) AS fraction
FROM players_on_next_day;


-- ================================================================================================================
-- Solution - 2

WITH first_login_day AS(
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
),

with_next_day AS(
    SELECT *, DATE_ADD(first_login, INTERVAL 1 DAY) AS next_day
    FROM first_login_day
)


SELECT ROUND((SELECT COUNT(*)
FROM Activity
WHERE (player_id, event_date) IN
(SELECT player_id, next_day  FROM with_next_day)) / 
(SELECT COUNT(DISTINCT(player_id)) FROM Activity), 2)
AS fraction;
