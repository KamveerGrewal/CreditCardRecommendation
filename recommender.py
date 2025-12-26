import pandas as pd

cards_df = pd.read_csv('CanadianCreditCards2025.csv')
users_df = pd.read_csv('generated_users.csv')

def calculate_card_value(user, card):
    """
    Calculates the Net Annual Value of a card.

    Formula = (Spend*Multiplier) + Welcome Bonus - Annual Fee
    """

    if user['Annual_Income'] < card['Min_Income_Personal'] and user['Annual_Income'] < card['Min_Income_Household']:
        return -9999
    
    if user['Credit_Score'] < card['Rec_Credit_Score']:
        return -9999
    
    # if user fails these, its never recomended.

    # rewards calculations (yearly):

    rewards_earned = (
        (user['Monthly_Spend_Grocery'] * card['Multiplier_Grocery']) +
        (user['Monthly_Spend_Dining'] * card['Multiplier_Dining']) +
        (user['Monthly_Spend_Gas'] * card['Multiplier_Gas']) +
        (user['Monthly_Spend_Travel'] * card['Multiplier_Travel']) +
        (user['Monthly_Spend_Other'] * card['Multiplier_Base'])
    ) * 12 

    # adjust for value of point (AMEX points worth more)

    rewards_value = rewards_earned *.01

    # net value is 50% of welcome bonus plus first year value

    adjusted_welcome_bonus = card['Welcome_Bonus_Est_Value'] * 0.5
    
    net_value = rewards_value + adjusted_welcome_bonus - card['Annual_Fee']
    
    return net_value

recommendations = []

for index, user in users_df.iterrows():
    print(f"Processing User {user['User_ID']}...")
    best_card = None
    max_value = -10000

    for id, card in cards_df.iterrows():
        value = calculate_card_value(user, card)

        if value > max_value:
            max_value = value
            best_card = card['Card_Name']

    recommendations.append({
        'User_ID': user['User_ID'],
        'Income': user['Annual_Income'],
        'Score': user['Credit_Score'],
        'Best_Card': best_card,
        'Est_Annual_Value': round(max_value, 2)
    })

results_df = pd.DataFrame(recommendations)

# Show the first 10 recommendations
print(results_df.head(1000))

# Save to file
results_df.to_csv('final_recommendations.csv', index=False)
print("\nSuccess! Recommendations saved to 'final_recommendations.csv'")