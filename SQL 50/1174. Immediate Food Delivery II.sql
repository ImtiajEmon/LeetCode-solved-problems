Solution - 1

WITH date_rank AS(
    SELECT *,
    RANK() OVER(PARTITION BY customer_id ORDER BY order_date) AS 'date_rank'
    FROM Delivery
)

SELECT ROUND((((
    SELECT count(*)
    FROM date_rank
    WHERE date_rank = 1 AND order_date = customer_pref_delivery_date
) / (SELECT COUNT(DISTINCT(customer_id)) FROM Delivery)) * 100), 2) AS 'immediate_percentage';

====================================================================================================
Solution - 2

WITH table_with_rankandtype AS(
    SELECT *,
    RANK() OVER(PARTITION BY customer_id ORDER BY order_date) AS order_rank,
    CASE WHEN order_date = customer_pref_delivery_date THEN
        'immediate'
    ELSE
        'scheduled'
    END AS order_type
    FROM Delivery
)

SELECT ROUND(SUM(
    CASE WHEN order_type = 'immediate' THEN 1
    ELSE 0 END
    ) / COUNT(*) * 100, 2) AS immediate_percentage
FROM table_with_rankandtype
WHERE order_rank = 1;

