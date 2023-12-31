CREATE TABLE users (
    USER_ID__DEID TEXT PRIMARY KEY,
    USER_TYPE TEXT NOT NULL,
    YEAR_OF_BIRTH FLOAT,
    DIABETES_TYPE TEXT
);

COPY users (USER_ID__DEID, USER_TYPE, YEAR_OF_BIRTH, DIABETES_TYPE) FROM '/tmp/final_subset_users_df__2023_02_27.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE device_syncs (
    SYNC_ID SERIAL PRIMARY KEY,
    USER_ID__DEID TEXT NOT NULL,
    SOURCE_TYPE TEXT NOT NULL,
    SYNC_TS__UTC TIMESTAMP NOT NULL
);

COPY device_syncs (USER_ID__DEID, SOURCE_TYPE, SYNC_TS__UTC) FROM '/tmp/final_subset_device_syncs_df__2023_02_27.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE webapp_pageviews (
    VIEW_ID SERIAL PRIMARY KEY,
    USER_ID__DEID TEXT NOT NULL,
    SESSION_TS TIMESTAMP NOT NULL,
    N_PAGES_VIEWED_IN_SESSION INTEGER NOT NULL,
    SESSION_DURATION__MINUTES INTEGER NOT NULL
);

COPY webapp_pageviews (USER_ID__DEID, SESSION_TS, N_PAGES_VIEWED_IN_SESSION, SESSION_DURATION__MINUTES) FROM '/tmp/final_subset_webapp_page_views_df__2023_02_27.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE bridge_clinics_to_patients (
    CLINIC_PATIENT_ID SERIAL PRIMARY KEY,
    CLINIC_ID__DEID TEXT NOT NULL,
    USER_ID__DEID TEXT NOT NULL
);

COPY bridge_clinics_to_patients (CLINIC_ID__DEID, USER_ID__DEID) FROM '/tmp/final_subset_bridge_clinics_to_patients_df__2023_02_27.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE bridge_clinics_to_professionals (
    CLINIC_PROFESSIONAL_ID SERIAL PRIMARY KEY,
    CLINIC_ID__DEID TEXT NOT NULL,
    USER_ID__DEID TEXT NOT NULL
);

COPY bridge_clinics_to_professionals (CLINIC_ID__DEID, USER_ID__DEID) FROM '/tmp/final_subset_bridge_clinics_to_professionals_df__2023_02_27.csv' DELIMITER ',' CSV HEADER;
