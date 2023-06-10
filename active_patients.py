import matplotlib.pyplot as plt 
import pandas as pd


df_device_syncs = pd.read_csv('database/final_subset_device_syncs_df__2023_02_27.csv')
df_device_syncs['date'] = pd.to_datetime(df_device_syncs['SYNC_TS__UTC']).dt.date
df_device_syncs['week'] = pd.to_datetime(df_device_syncs['SYNC_TS__UTC']).dt.week

active_professionals_daily = df_device_syncs.groupby(['date'])['USER_ID__DEID'].nunique()
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(active_professionals_daily.index, active_professionals_daily.values)
plt.xlabel('Weekaily')
plt.ylabel('Daily Active Patients')
plt.title('Daily Trend of Active Patients')

# Save the plot as a .png file
plt.savefig('plots/daily_trend_active_patients.png')

plt.show()

active_professionals = df_device_syncs.groupby(['week'])['USER_ID__DEID'].nunique()
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(active_professionals.index, active_professionals.values)
plt.xlabel('Week')
plt.ylabel('Active Patients')
plt.title('Weekly Trend of Active Patients')

# Save the plot as a .png file
plt.savefig('plots/weekly_trend_active_patients.png')

plt.show()

df_users = pd.read_csv('database/final_subset_users_df__2023_02_27.csv')
df_users_devices = df_device_syncs.merge(df_users, how='left')
diabetes_type1 = df_users_devices[df_users_devices['DIABETES_TYPE']=='type_1'].groupby(['week'])['USER_ID__DEID'].nunique()
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(diabetes_type1.index, diabetes_type1.values)
plt.xlabel('Week')
plt.ylabel('Active Patients Diabetes Type1')
plt.title('Trend of Diabetes Type1 Active Patients Per Week')

# Save the plot as a .png file
plt.savefig('plots/total_active_patients_type1_diabetes.png')

plt.show()



diabetes_type2 = df_users_devices[df_users_devices['DIABETES_TYPE']=='type_2'].groupby(['week'])['USER_ID__DEID'].nunique()
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(diabetes_type2.index, diabetes_type2.values)
plt.xlabel('Week')
plt.ylabel('Active Patients Diabetes Type2')
plt.title('Trend of Diabetes Type2 Active Patients Per Week')

# Save the plot as a .png file
plt.savefig('plots/total_active_patients_type2_diabetes.png')

plt.show()