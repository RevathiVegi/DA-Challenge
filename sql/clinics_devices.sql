SELECT c.CLINIC_ID__DEID, d.SOURCE_TYPE, COUNT(*) 
FROM device_syncs d
JOIN bridge_clinics_to_patients c ON c.USER_ID__DEID = d.USER_ID__DEID 
GROUP BY c.CLINIC_ID__DEID, d.SOURCE_TYPE;