import matplotlib.pyplot as plt
import pandas as pd


df_clinics_patients = pd.read_csv('database/final_subset_bridge_clinics_to_patients_df__2023_02_27.csv')
df_device_syncs = pd.read_csv('database/final_subset_device_syncs_df__2023_02_27.csv')
df_device_syncs['date'] = pd.to_datetime(df_device_syncs['SYNC_TS__UTC']).dt.date
df_device_syncs['week'] = pd.to_datetime(df_device_syncs['SYNC_TS__UTC']).dt.week
df_clinics = df_clinics_patients.merge(df_device_syncs, how='left')

clinics_daily_trend = df_clinics.groupby(['date'])['CLINIC_ID__DEID'].nunique()
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(clinics_daily_trend.index, clinics_daily_trend.values)
plt.xlabel('Date')
plt.ylabel('Number of Clinics')
plt.title('Daily Trend of Patient Clinics')

# Save the plot as a .png file
plt.savefig('plots/daily_clinics_trends.png')

plt.show()

clinics_weekly_trend = df_clinics.groupby(['week'])['CLINIC_ID__DEID'].nunique()
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(clinics_weekly_trend.index, clinics_weekly_trend.values)
plt.xlabel('Week')
plt.ylabel('Number of Clinics')
plt.title('Weekly Trend of Patient Clinics')

# Save the plot as a .png file
plt.savefig('plots/weekly_clinics_trends.png')

plt.show()