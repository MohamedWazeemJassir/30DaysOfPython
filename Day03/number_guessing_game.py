import random

LEADERBOARD_FILE = "leaderboard.txt"

# Generate a random number and assign it to a variable
def get_random_number(min_value, max_value):
	secret_number = random.randint(min_value, max_value)
	return secret_number

def print_greeting():
	print("\n\nWelcome to Number Guessing Game\n")

# Print Menu and get difficulty level as input
def print_menu():
	print("Select Difficulty Levels:")
	print("1. Easy (Range 1 to 20), 10 attempts")
	print("2. Medium (Range 1 to 50), 8 attempts")
	print("3. Hard (Range 1 to 100), 5 attempts")

def get_difficulty_level():
	difficulty = int(input("Enter your difficulty range (1/2/3):"))
	return difficulty

# Set minimum value, Maximum value and maximum attempts
def get_min_max_attempts_for_difficulty_level(difficulty):
	if difficulty == 1:
		min_value, max_value, max_attempts = 1, 20, 10
	elif difficulty == 2:
		min_value, max_value, max_attempts = 1, 50, 8
	elif difficulty == 3:
		min_value, max_value, max_attempts = 1, 100, 5
	# Validation for number other than 1, 2, 3
	return min_value, max_value, max_attempts

# Get Winner's name
def get_winners_detail():
	name = input("Player Name : ")
	return name

# Read the file and get leaderboard data
def show_leaderboard():
	with open(LEADERBOARD_FILE, "r") as fp:
		leaderboard = [line.strip().split(",") for line in fp.readlines()]
		leaderboard = [(name, int(level), int(attempts)) for name, level, attempts in leaderboard]
		
# Update and save leaderboard
def update_leaderboard():
	pass

def save_leaderboard(name, difficulty_level, no_of_attempts):
	with open(LEADERBOARD_FILE, "a") as fp:
		fp.write(f"{name},{difficulty_level},{no_of_attempts}")
	
# Game Logic
def play():
	difficulty = get_difficulty_level()
	min_value, max_value, max_attempts = get_min_max_attempts_for_difficulty_level(difficulty)
	
	secret_number = get_random_number(min_value, max_value)
	# print("Secret Number is ", secret_number)
	atempts = 0
	
	while True:
		guess = int(input("Enter your predicted value : "))
		atempts = atempts + 1
		
		if guess < secret_number:
			print("Too Low !!! Try another number\n")
		elif guess > secret_number:
			print("Too High !!! Try another number\n")
		else:
			print("Congratulations !!! you have found the number in "+ str(atempts) + " attempts")
			player_name = get_winners_detail()
			save_leaderboard(player_name, difficulty, atempts)
			break
			
		if atempts == max_attempts:
			print("Sorry !  You have exhausted max attempts\n")
			break

# Ask whether the user wants to play the game again
def play_again():
	play_again = input("Do you want to play again !!! (Y/N)")
	if play_again.lower() == "y":
		number_guessing_game()
	else:
		print("Thank You for playing !!! See you again\n")

# Use functions to run the game
def number_guessing_game():
	print_greeting()
	print_menu()
	play()
	play_again()
	
number_guessing_game()
	
