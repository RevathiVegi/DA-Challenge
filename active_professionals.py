import matplotlib.pyplot as plt 
import pandas as pd


df_webapp_page_views = pd.read_csv('database/final_subset_webapp_page_views_df__2023_02_27.csv')
df_webapp_page_views['date'] = pd.to_datetime(df_webapp_page_views['SESSION_TS']).dt.date
df_webapp_page_views['week'] = pd.to_datetime(df_webapp_page_views['SESSION_TS']).dt.week
active_professionals_day = df_webapp_page_views.groupby(['date'])['USER_ID__DEID'].nunique()
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(active_professionals_day.index, active_professionals_day.values)
plt.xlabel('Daily')
plt.ylabel('Active Professionals')
plt.title('Daily Trend of Active Professionals')

# Save the plot as a .png file
plt.savefig('plots/daily_trend_active_professionals.png')

plt.show()


active_professionals = df_webapp_page_views.groupby(['week'])['USER_ID__DEID'].nunique()
plt.figure(figsize=(10, 6))
plt.plot(active_professionals.index, active_professionals.values)
plt.xlabel('Week')
plt.ylabel('Active Professionals')
plt.title('weekly Trend of Active Professionals')

# Save the plot as a .png file
plt.savefig('plots/weekly_trend_active_professionals.png')

plt.show()