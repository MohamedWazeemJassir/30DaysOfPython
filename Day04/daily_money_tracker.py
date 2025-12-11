import csv
import os
from datetime import datetime

CSV_FILE = "daily_expense.csv"

def check_file_exists_or_create_and_add_header():
	if not os.path.exists(CSV_FILE):
		with open(CSV_FILE, "w", newline="") as f:
			writer = csv.writer(f)
			writer.writerow(["expense_id", "date", "category", "amount", "note"])
		print("Created daily_expense.csv")

# Print Menu
def print_menu():
	print("\n######### DAILY TRACKER ####### \n")
	print("1. Add Expense")
	print("2. View Expense")
	print("3. Monthly Summary")
	print("4. Edit an Expense")
	print("Press any other to exit")

# Get date and expense data and add it to csv file
def add_expense():
	date = input("Enter date (YYYY-MM-DD): ")
	category = input("Enter category (Food/Travel/Bills etc) : ")	
	amount = float(input("Enter amount : "))
	note = input("Enter note : ")
	
	expense_id = int(datetime.now().timestamp())
	
	with open(CSV_FILE, "a", newline="") as f:
		writer = csv.writer(f)
		writer.writerow([expense_id, date, category, amount, note])
	
	print(f"Expense added {expense_id}, {amount}")
	
# Read and display data from csv file
def view_expense():
	with open(CSV_FILE, "r") as f:
		reader = csv.reader(f)
	
		for row in reader:
			print(row)
	
	print("\n Viewed all expenses ")
	
# Create monthly summary
def monthly_summary():
	month = input("Enter month (YYYY-MM) : ")
	total = 0
	
	with open(CSV_FILE, "r") as f:
		reader = csv.reader(f)
		
		for row in reader:
			print("Row Value is ", row)
			expense_value = row
			if expense_value[1].startswith(month):
				total = total + float(expense_value[3])
	
	print(f"Total Expenses for {month}: Rs. {total}")
	
# Edit Expense data
def edit_an_expense():
	expense_id = input("Enter expense Id : ")
	data = []
	found = False
	with open(CSV_FILE, "r") as f:
		rows = csv.reader(f)
		
		for row in rows:
			if row[0] == expense_id:
				found = True
				print("Current Row : ", row)
				# [expense_id, date, category, amount, note]
				#     0         1      2         3       4
				row[1] = input("Enter Date (YYYY-MM-DD ) : ") or row[1]
				row[2] = input("Enter category : ") or row[2]
				row[3] = float(input("Enter amount : ")) or row[3]
				row[4] = input("Enter Description : ") or row[4]
			data.append(row)
			
		if not found:
			print("Expense ID is not Found")
			return
		
	with open(CSV_FILE, "w") as f:
		writer = csv.writer(f)
		writer.writerows(data)
	print(f"Expense Id {expense_id} is updated")

# Use functions to create the tracker
def daily_tracker():
	check_file_exists_or_create_and_add_header()
	
	while True:
		print_menu()
		user_action = int(input("Enter your choice : "))
		
		if user_action == 1:
			add_expense()
		elif user_action == 2:
			view_expense()
		elif user_action == 3:
			monthly_summary()
		elif user_action == 4:
			edit_an_expense()
		else:
			print("Thanks for Using !!! ")
			break

daily_tracker()

