import pandas as pd
import numpy as np

# 1. Create a sample dataset (Simulating a CSV bank statement)
data = {
    'Date': ['2026-03-01', '2026-03-02', '2026-03-05', '2026-03-10', '2026-03-15', '2026-03-20'],
    'Description': ['Starbucks Coffee', 'Apartment Rent', 'Netflix Subscription', 'Whole Foods Market', 'Shell Gas Station', 'Steam Games'],
    'Amount': [5.50, 1200.00, 15.99, 85.20, 45.00, 59.99]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# 2. Define Categorization Logic using NumPy
# We use np.select to assign categories based on keywords in the description
conditions = [
    df['Description'].str.contains('Starbucks|Foods', case=False),
    df['Description'].str.contains('Rent', case=False),
    df['Description'].str.contains('Netflix|Games', case=False),
    df['Description'].str.contains('Gas|Shell', case=False)
]
categories = ['Food & Dining', 'Housing', 'Entertainment', 'Transportation']

df['Category'] = np.select(conditions, categories, default='Other')

# 3. Identify "High" vs "Low" Expenses using NumPy
# If amount > 100, it's a "Major" expense, otherwise "Minor"
df['Expense_Type'] = np.where(df['Amount'] > 100, 'Major', 'Minor')

# 4. Generate a Summary Report using Pandas
summary = df.groupby('Category')['Amount'].agg(['sum', 'count']).reset_index()
summary.columns = ['Category', 'Total Spent', 'Transaction Count']

# 5. Calculate Percentage of Total Spending
total_monthly_spend = df['Amount'].sum()
summary['Percentage'] = (summary['Total Spent'] / total_monthly_spend * 100).round(2)

print("--- Categorized Transactions ---")
print(df)
print("\n--- Spending Summary ---")
print(summary)