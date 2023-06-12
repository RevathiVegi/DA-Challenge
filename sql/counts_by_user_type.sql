SELECT
    COUNT(DISTINCT CASE WHEN USER_TYPE = 'Patient' THEN user_id__deid END) AS Patient,
    COUNT(DISTINCT CASE WHEN USER_TYPE = 'Professional' THEN user_id__deid END) AS Professional,  
    COUNT(DISTINCT CASE WHEN USER_TYPE in ('Patient','Professional') THEN user_id__deid END) AS Combined
FROM users;
