# Get user intent
print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. View Calculation History
6. Power
7. Floor Division
8. Press 8 to exit.
""")

calculator_condition = True
history = []

# Task 4 - Use functions
def store_calculations(operation_name, input_values, result):
	history.append([operation_name, input_values, result])

def add():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 + number_2
	print("The result is", result)
	store_calculations("Add", (number_1, number_2), result)

def subtract():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 - number_2
	print("The result is", result)
	store_calculations("Subtract", (number_1, number_2), result)

def multiply():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 * number_2
	print("The result is", result)
	store_calculations("Multiply", (number_1, number_2), result)

def divide():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))

	# Task 1 - Handle Division by Zero. 
	if number_2 == 0:
			print("Error: Division by zero is not allowed.")
	else:
		result = number_1 / number_2
		print("The result is", result)
		store_calculations("Divide", (number_1, number_2), result)

# Task 3 - Add advanced operations (Modulus, Power, Floor Division)
def modulus():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 % number_2
	print("The result is", result)
	store_calculations("Modulus", (number_1, number_2), result)	

def power():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 ** number_2
	print("The result is", result)	
	store_calculations("Power", (number_1, number_2), result)

def floor_division():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	if number_2 == 0:
			print("Error: Division by zero is not allowed.")
	else:
		result = number_1 // number_2
		print("The result is", result)
		store_calculations("Floor Division", (number_1, number_2), result)

while calculator_condition:
	print("\n")
	print("Welcome to calculator !")

	user_operation = int(input("Enter your option: "))

	if user_operation == 1:
		# Addition Logic
		print("Addition")
		add()
		
	elif user_operation == 2:
		# Subtraction Logic
		print("Subtract")
		subtract()
		
	elif user_operation == 3:
		# Multiplication Logic
		print("Multiplication")
		multiply()
		
	elif user_operation == 4:
		# Division Logic
		print("Division")
		divide()
		
	elif user_operation == 5:
		# Modulus Logic
		print("Modulus")
		modulus()

	elif user_operation == 6:
		print()
		if history == []:
			print("No calculations done yet.")
		else:
			for _ in history:
				print(_)
		
	elif user_operation == 7:
		# Power Logic
		print("Power")
		power()
		
	elif user_operation == 8:
		# Floor Division Logic
		print("Floor Division")
		floor_division()
	
	elif user_operation == 9:
		print("Thanks for using calculator! See you again.")
		calculator_condition = False

	# Task 2 - Invalid Choice Handling: 
	# If user enters an invalid menu option, show, "Please select a valid operation (1–4)"
	else:
		print("Please select a valid operation (1–8).")

