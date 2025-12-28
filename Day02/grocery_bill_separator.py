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

# Print all items
grand_total = 0
for item in bill_items:
	print(item)
	grand_total += item[2]

print("Grand total: ", grand_total)
