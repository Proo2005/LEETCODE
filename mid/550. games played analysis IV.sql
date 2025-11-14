SELECT 
    ROUND(
        COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM (
    SELECT a.player_id
    FROM Activity a
    JOIN (
        SELECT player_id, MIN(event_date) AS first_date
        FROM Activity
        GROUP BY player_id
    ) f
    ON a.player_id = f.player_id 
       AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)
) AS next_day_login;
