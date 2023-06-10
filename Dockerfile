# Use an official Postgres runtime as a parent image
FROM postgres:latest

# Set environment variables for the database
ENV POSTGRES_USER postgres_user
ENV POSTGRES_PASSWORD postgres_password
ENV POSTGRES_DB my_db

# Copy the .csv file into the container
COPY database/final_subset_bridge_clinics_to_patients_df__2023_02_27.csv /tmp/final_subset_bridge_clinics_to_patients_df__2023_02_27.csv
COPY database/final_subset_bridge_clinics_to_professionals_df__2023_02_27.csv /tmp/final_subset_bridge_clinics_to_professionals_df__2023_02_27.csv
COPY database/final_subset_device_syncs_df__2023_02_27.csv /tmp/final_subset_device_syncs_df__2023_02_27.csv
COPY database/final_subset_users_df__2023_02_27.csv /tmp/final_subset_users_df__2023_02_27.csv
COPY database/final_subset_webapp_page_views_df__2023_02_27.csv /tmp/final_subset_webapp_page_views_df__2023_02_27.csv


# Copy the script to load the data into the container
COPY database/load_data.sql /docker-entrypoint-initdb.d/

# Set the permissions on the script
RUN chmod 755 /docker-entrypoint-initdb.d/load_data.sql
