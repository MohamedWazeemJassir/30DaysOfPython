# Declare cost in a dictionary
commodity_price = {
	"rice": 40,
	"wheat": 50,
	"egg": 6,
	"oil": 118,
	"curd": 10,
	"carrot": 90
}

groceries = []
user_picked_commodity = {}
bill_items = []

# Task 5 - Create functions
def display_items():
	print("Items available are:")
	for key, value in commodity_price.items():
		print(key.capitalize())
	print()

def get_user_items():
	# Get number of items as input
	total_items = int(input("Enter Total Grocery Items : "))
	for itr in range(total_items):
		# Get item name and weight
		grocery_name = input("Enter grocery item name: " + str(itr + 1) + " ")
		
		# Task 1 - Validate Commodity Name
		if grocery_name not in commodity_price:
			print("Item not available")
			grocery_name = input("Enter grocery item name: " + str(itr + 1) + " ")
		weight = float(input("Enter weight of " + grocery_name + ": "))

		# Append item name to list an d calculate price
		groceries.append(grocery_name)
		user_picked_commodity[grocery_name] = weight * commodity_price.get(grocery_name, 0)
		
		# Create each item's bill as tuple and append it to final bill list
		billed_res = (
						grocery_name,
						weight,
						commodity_price.get(grocery_name, 0),
						user_picked_commodity.get(grocery_name)
						)
		bill_items.append(billed_res)

def calculate_bill():
	# Task 2 - Find the grand total. 
	grand_total = 0
	for item in bill_items:
		grand_total += item[3]
	# Task 4 - Add 5% GST on total amount on all commodities.
	grand_total += grand_total * 0.05
	if grand_total > 500:
		grand_total -= grand_total * 0.1
	elif grand_total > 1000:
		grand_total -= grand_total * 0.15
	return grand_total

def print_bill():
	# Task 3 - Pretty Bill Format
	print("\nItem\tWeight\tPrice\tAmount")
	print("---------------------------------")
	for item in bill_items:
		print(f"{item[0]}\t{item[1]}kg\t{item[2]}\t{item[3]}")
	print("---------------------------------\n")
	print("Grand total: ", calculate_bill())

display_items()
get_user_items()
print_bill()

