import pandas as pd

df = pd.read_csv('final_recommendations.csv')

# FIX: was getting negative average from users with annual value of -9999
# so we will filter them out for a more accurate result
successful_recs = df[df['Est_Annual_Value'] > -1000]
failed_recs = df[df['Est_Annual_Value'] <= -1000]

card_counts = df['Best_Card'].value_counts().reset_index()
card_counts.columns = ['Card_Name', 'Recommendation_Count']

avg_value = successful_recs['Est_Annual_Value'].mean()

print(f"\n--- ANALYSIS REPORT ---")
print(f"Total Users Processed: {len(df)}")
print(f"Average Annual Value Generated: ${avg_value:.2f}")
print(f"\nTop 5 Most Recommended Cards:")
print(card_counts.head(5))

# Since Cobalt is regarded as best card in Canada by many
cobalt_users = df[df['Best_Card'] == 'Amex Cobalt']
print(f"\nAverage Income of Amex Cobalt Users: ${cobalt_users['Income'].mean():.2f}")