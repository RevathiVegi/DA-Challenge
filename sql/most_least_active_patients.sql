(SELECT CLINIC_ID__DEID, COUNT(DISTINCT USER_ID__DEID) as active_patients 
FROM bridge_clinics_to_patients 
WHERE USER_ID__DEID IN (
    SELECT USER_ID__DEID FROM device_syncs
) 
GROUP BY CLINIC_ID__DEID 
ORDER BY active_patients DESC
LIMIT 1)

UNION ALL

(SELECT CLINIC_ID__DEID, COUNT(DISTINCT USER_ID__DEID) as active_patients 
FROM bridge_clinics_to_patients 
WHERE USER_ID__DEID IN (
    SELECT USER_ID__DEID FROM device_syncs
) 
GROUP BY CLINIC_ID__DEID 
ORDER BY active_patients
LIMIT 1);
