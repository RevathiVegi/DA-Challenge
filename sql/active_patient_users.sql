SELECT 
    COUNT(DISTINCT CASE WHEN SYNC_TS__UTC >= NOW() - INTERVAL '1 year' THEN USER_ID__DEID END) AS active_patient_users_past_year,
    COUNT(DISTINCT CASE WHEN SYNC_TS__UTC >= NOW() - INTERVAL '1 month' THEN USER_ID__DEID END) AS active_patient_users_past_month
FROM 
    device_syncs
WHERE 
    USER_ID__DEID IN (
        SELECT USER_ID__DEID 
        FROM users 
        WHERE USER_TYPE = 'Patient'
    );

