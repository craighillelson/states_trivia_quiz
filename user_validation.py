# choose a category
# then choose a number of states to drill in that category

''' 
while True:
	try:
		user_input = int(raw_input("Please enter an integer: "))
		break
	except ValueError:
		print("That is not an integer. Please try again. ")

print("Thanks! You entered %s.") % (user_input)
'''

while True:
	try:
		user_input = (raw_input("Please choose a category: A, B, or C: "))
		break
	except ValueError:
		while user_input not in ['A', 'B', 'C']:
			print("That is not an integer. Please try again. ")

print("Thanks! You entered %s.") % (user_input)