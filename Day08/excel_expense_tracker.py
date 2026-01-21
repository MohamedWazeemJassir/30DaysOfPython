import pandas as pd
import os
from datetime import datetime

EXCEL_FILENAME = "modular_finances.xlsx"

# Initialize tracker
def initialize_tracker():
    return {
        'expenses': [],
        'savings': []
    }

# load data from excel file
def load_from_excel(filename=EXCEL_FILENAME):
    tracker_data = initialize_tracker()
    
    if not os.path.exists(filename):
        return tracker_data
    
    try:
        df_expenses = pd.read_excel(filename, sheet_name='Expenses')
        tracker_data['expenses'] = df_expenses.to_dict('records')
    except Exception:
        pass

    try:
        df_savings = pd.read_excel(filename, sheet_name='Savings')
        tracker_data['savings'] = df_savings.to_dict('records')
    except Exception:
        pass

    return tracker_data

# Add transactions
def add_transaction(tracker_data, type, amount, category, description=""):
    try:
        amount = float(amount)
    except ValueError:
        return

    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    record = {
        'Date': date_str,
        'Amount': amount,
        'Category': category,
        'Description': description
    }

    if type.lower() == 'expense':
        tracker_data['expenses'].append(record)
    elif type.lower() == 'saving':
        tracker_data['savings'].append(record)
    else:
        pass

# Saves data to excel file
def save_to_excel(tracker_data, filename=EXCEL_FILENAME):
    expenses = tracker_data.get('expenses', [])
    savings = tracker_data.get('savings', [])

    if not expenses and not savings:
        return

    df_expenses = pd.DataFrame(expenses)
    df_savings = pd.DataFrame(savings)

    try:
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            if not df_expenses.empty:
                df_expenses.to_excel(writer, sheet_name='Expenses', index=False)

            if not df_savings.empty:
                df_savings.to_excel(writer, sheet_name='Savings', index=False)

    except Exception:
        pass

def main():
    finance_data = load_from_excel()
    
    add_transaction(finance_data, 'expense', 19.99, 'Entertainment', 'Movie ticket')
    add_transaction(finance_data, 'saving', 50.00, 'Refund', 'Returned item')

    save_to_excel(finance_data)

if __name__ == "__main__":
    main()
