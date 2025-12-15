import pandas as pd
import os
from datetime import datetime

tracker = {
	"expenses": [],
	"savings": []
}

TRANSACTION_FILE = "expense_tracker.xlsx"

def add_transaction(transaction_type, amount, category, description=""):
	amount = float(amount)
	date_str = datetime.now().strftime("%Y-%m-%d")
	
	record = {
		"Date": date_str,
		"Amount": amount,
		"Category": category,
		"Description": description
	}
	
	if t
	
	df_expenses = pd.DataFrame(expenses)
	df_savings = pd.DataFransaction_type.lower() == "expense":
		tracker["expenses"].append(record)
	elif transaction_type.lower() == "savings":
		tracker["savings"].append(record)

def save_to_excel(filename=TRANSACTION_FILE):
	
	expenses = tracker.get("expenses", [])
	savings = tracker.get("savings", [])rame(savings)
	
	with pd.ExcelWriter(filename, engine="openpyxl") as writer:
		df_expenses.to_excel(writer, sheet_name = "Expenses")
		df_savings.to_excel(writer, sheet_name = "Savings")
	


def get_transactional_input():
	transaction_type = input("Enter transaction Type : ")
	amount = input("How much ? ")
	category = input("Where did you spent/saved ? ")
	description = input("Any Descriptions ? ")
	
	return transaction_type, amount, category, description

print("Welcome to transactional data")


another_transaction = True

while another_transaction:

	transaction_type, amount, category, description = get_transactional_input()
	add_transaction(transaction_type, amount, category, description)
	
	next_iteration = input("Do you want to add another transaction ? Y/N ")
	if next_iteration.lower() == "n":
		another_transaction = False
		
save_to_excel()















	
