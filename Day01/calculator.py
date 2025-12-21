# Get user intent
print("""
1. Addition \n
2. Subtraction \n
3. Multiplication \n
4. Division \n
5. Modulus \n
6. Power \n
7. Floor Division \n
8. Press 8 to exit.
""")

calculator_condition = True

# Define functions for each operation
def add():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 + number_2
	print("The result is", result)

def subtract():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 - number_2
	print("The result is", result)

def multiply():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 * number_2
	print("The result is", result)

def divide():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	if number_2 == 0:
			print("Error: Division by zero is not allowed.")
	else:
		result = number_1 / number_2
		print("The result is", result)

def modulus():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 % number_2
	print("The result is", result)	

def power():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 ** number_2
	print("The result is", result)	

def floor_division():
	number_1 = int(input(" Enter number 1 "))
	number_2 = int(input(" Enter number 2 "))
	result = number_1 // number_2
	print("The result is", result)	

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
		# Power Logic
		print("Power")
		power()
		
	elif user_operation == 7:
		# Floor Division Logic
		print("Floor Division")
		floor_division()
	
	elif user_operation == 8:
		print("Thanks for using calculator ! See you again.")
		calculator_condition = False

	else:
		print("Invalid input. Enter a valid number.")

