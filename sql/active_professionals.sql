SELECT 
    COUNT(DISTINCT CASE WHEN session_ts >= NOW() - INTERVAL '1 year' THEN USER_ID__DEID END) AS active_users_past_year,
    COUNT(DISTINCT CASE WHEN session_ts >= NOW() - INTERVAL '1 month' THEN USER_ID__DEID END) AS active_users_past_month
FROM 
    webapp_pageviews
WHERE 
    USER_ID__DEID IN (
        SELECT USER_ID__DEID 
        FROM users 
        WHERE USER_TYPE = 'Professional'
    );


