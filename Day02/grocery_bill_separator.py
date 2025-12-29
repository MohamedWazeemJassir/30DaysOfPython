# Declare cost in a dictionary
commodity_price = {
	"rice": 40,
	"wheat": 50,
	"egg": 6,
	"oil": 118,
	"curd": 10,
	"carrot": 90
}

# Get number of items as input
total_items = int(input("Enter Total Grocery Items :"))
print("Total Items", total_items)

groceries = []
user_picked_commodity = {}
bill_items = []

for itr in range(total_items):
	# Get item name and weight
	grocery_name = input("Enter grocery item name: " + str(itr) + " ")
	# Task 1 - Validate Commodity Name
	# If the user enters an item not in commodity_price then show, "Item not available". 
	# Ask the user to re-enter the item name.
	if grocery_name not in commodity_price:
		print("Item not available")
		grocery_name = input("Enter grocery item name: " + str(itr) + " ")
	weight = float(input("Weight of " + grocery_name + " "))

	# Append item name to list an d calculate price
	groceries.append(grocery_name)
	user_picked_commodity[grocery_name] = weight * commodity_price.get(grocery_name, 0)
 	
	# Create each item's bill as tuple and apeend it to final bill list
	billed_res = (
 					grocery_name,
 					weight,
 					commodity_price.get(grocery_name, 0),
 					user_picked_commodity.get(grocery_name)
 					)
	bill_items.append(billed_res)

# Print the groceries collected
print("Groceries collected ", user_picked_commodity)

# Task 2 - Find the grand total. 
grand_total = 0

# Task 3 - Pretty Bill Format
print("Item\tWeight\tPrice\tAmount")
print("---------------------------------")
for item in bill_items:
	print(f"{item[0]}\t{item[1]}kg\t{item[2]}\t{item[3]}")
	grand_total += item[3]

# Task 4 - Add 5% GST on total amount on all commodities.
grand_total += grand_total * 0.05

print("---------------------------------")
print("Grand total: ", grand_total)
