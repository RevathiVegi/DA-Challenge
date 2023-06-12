SELECT CLINIC_ID__DEID, COUNT(DISTINCT USER_ID__DEID) as active_professionals 
FROM bridge_clinics_to_professionals 
WHERE USER_ID__DEID IN (
    SELECT USER_ID__DEID FROM webapp_pageviews
) 
GROUP BY CLINIC_ID__DEID;


