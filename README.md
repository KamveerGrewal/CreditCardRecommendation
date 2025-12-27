**Canadian Credit Card Recommendation Engine**

### Overview

This project simulates a financial product recommendation engine. It matches Canadian users to the credit card based on their spending habits, income, credit score, and risk profile. 
The goal was to move beyond "filtering" and calculate the Net **Annual Value** for every user to maximize their financial return.

### Method
  **Data Engineering:** Built a dataset of 50+ Canadian credit cards (Scotiabank, TD, Amex, etc.) including fees, reward multipliers, and income gates.
  **User Simulation:** Generated 1,000 user profiles using Python (`numpy` log-normal distributions) to mimic real-world income and spending variance.
  **Logic Engine:** Developed a Python script to calculate the NAV for every user-card combination:
    * NAV = (Annual_Spend * Multipliers) + Welcome_Bonus - Annual_Fee

### Key Insights
  **The "Gold" Standard:** The **Scotiabank Gold Amex** was the most recommended card (36% of users). It consistently outperformed "No-Fee" cards for low-to-mid income users due to its 5x reward multiplier on dining/groceries.
  **Churning:** The average user generated **$1,183** in first-year value, largely because of Welcome Bonuses which the algorithm prioritized.
  **AMEX COBALT:** The engine deduced that the average income of Amex Cobalt card users was around 63k, which suggests the card is the optimal choice for "young professionals" who have moved past entry-level cards.

### How to Run
  1. Install dependencies: `pip install pandas numpy`
  2. Run the engine: `python recommender.py`
  3. View the analysis: `python analysis.py`
