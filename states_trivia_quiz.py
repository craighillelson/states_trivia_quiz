# imports
import csv
import random
from datetime import date

# define functions
def print_return():
	print("\n")

def quiz(a, b):
	# define variables
	print(category_header)
	print_return()
	correct = 0
	incorrect = 0
	# for the number of states the user specified to drill, generate an equal number of random numbers less than 50
	for j in i:
		print_return()
		state = states[j]
		state_formatted = "%s " % (state)
		# set 'a' equal to a random item in the chosen list (capitals, nicknames, or years_founded)
		a = b[j]
		user_answer = raw_input(state_formatted)
		# test the user's answer and respond 
		if user_answer == a:
			print("Correct. Good job!\n")
			correct = correct + 1
			corrects.append(state)
		else:
			incorrect = incorrect + 1
			incorrects.append(state)
			while True:
				see_the_answer_response = str(raw_input(see_the_answer+' (y or n): ')).lower().strip()
				if see_the_answer_response not in ['y', 'n']:
					print("invalid choice")
				# give user the correct answer
				elif see_the_answer_response == 'y':
					print("The correct answer is %s") % (b[j])
					break
				else:
					break

	# calculate and format percentage correct
	percentage_correct =  float(correct) / float(user_choice)
	percentage_formatted = "{0:.0%}".format(percentage_correct)
	print("Results: %s correct %s incorrect. %s\n") % (correct, incorrect, percentage_formatted)
	
	# update user with their results. if user got any wrong, write the states missed to a text file
	today = date.today()
	today = "%s.txt" % (today)
	with open(today, 'w') as results:
		if incorrect > 0:
			results.write("States to Review"+ "\n")
			print("States to brush up on:")
			for states_missed in incorrects:
				results.write(states_missed+ "\n")
				print(states_missed)
			print_return()
			print("Check %s to see where you can improve.") % (today)
			print_return()
		else:
			results.write("Great job!!! 100%")
			print("Great job!!! 100%")
			print_return()

# define lists to be populated later
states = []
capitals = []
nicknames = []
years_founded = []
orders = []
corrects = []
incorrects = []

# import csv
with open('states_trivia.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		capital = row['capital']
		nickname = row['nickname']
		year_founded = row['year founded']
		states.append(row['state'])
		capitals.append(row['capital'])
		nicknames.append(row['nickname'])
		years_founded.append(row['year founded'])
		orders.append(row['order'])

# get length of the list of states
number_of_states = len(states)

# define questions
category = "Would you like to drill a - capitals, b - nicknames, or c - years founded? "
question = "How many states would you like to drill in that category? (select an integer between 1 and %s) " % (number_of_states)
see_the_answer = "Sorry, that's incorrect. Would you like to see the correct answer?"

# define responses
too_many = "Please select an integer less than %s " % (number_of_states)
not_an_integer = "That won't work. Please enter an integer between 1 and 50. "

# prompt user to select a category
while True:
	category_choice = str(raw_input(category)).lower().strip()
	if category_choice not in ['a', 'b', 'c']:
		print("invalid choice")
	else:
		if category_choice == 'a':
			print("you selected %s - capitals") % (category_choice)
			category_header = "Type the capital of each state."
		elif category_choice == 'b':
			print("you selected %s - nicknames") % (category_choice)
			category_header = "Type the nickname of each state."
		else:
			print("you selected %s - years founded") % (category_choice)
			category_header = "Type the year each state joined the union."
		break

# prompt user to select how many states they'd like to drill
while True:
	try:
		user_choice = int(raw_input(question))
	except ValueError:
		print("Please enter an integer.")
		continue
	if user_choice > number_of_states:
		print("Please enter an integer between 1 and 50.")
	else:
		break

# define i
i = random.sample(range(number_of_states), int(user_choice))

# prompt user
if category_choice == 'a':
	quiz(capital, capitals)
elif category_choice == 'b':
	quiz(nickname, nicknames)
else:
	quiz(year_founded, years_founded)
