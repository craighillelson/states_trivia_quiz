# imports
import csv
import random

# define function
def print_return():
	print("\n")

# define lists to be populated later
states = []
capitals = []
corrects = []
incorrects = []

# import csv
with open('states_and_capitals.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		states.append(row['state'])
		capitals.append(row['capital'])

# get length of the list of states
number_of_states = len(states)

# define reponses
question = "How many states and capitals would you like to drill? (select an integer between 1 and %s) " % (number_of_states)
too_many = "Please select an integer less than %s " % (number_of_states)
not_an_integer = "That won't work. Please enter an integer between 1 and 50. "

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

# define i, set counters to 0
i = random.sample(range(number_of_states), int(user_choice))
correct = 0
incorrect = 0

# prompt user
for j in i:
	print_return()
	state = states[j]
	state_formatted = "%s " % (state)
	capital = capitals[j]
	user_answer = raw_input(state_formatted)
	if user_answer == capital:
		print("Correct. Good job!\n")
		correct = correct + 1
	else:
		print("Sorry. That's incorrect.\n")
		incorrect = incorrect + 1
		incorrects.append(state)

# update user on their performance
percentage_correct =  float(correct) / float(user_choice)
percentage_formatted = "{0:.0%}".format(percentage_correct)
print("Results: %s correct %s incorrect. %s\n") % (correct, incorrect, percentage_formatted)