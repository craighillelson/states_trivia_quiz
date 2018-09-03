# import
import csv

# define lists to be populated later
states = []
dates_entered = []

with open('state_entered_union.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		state = row['state']
		entered_union = row['entered_union']
		# print("%s, %s") % (state, entered_union)
		states.append(state)
		dates_entered.append(entered_union)

# sort alphabetically
states.sort()

# loop through states and print results
for state in states:
	print(state)

# sort in reverse order
dates_entered.sort(reverse = True)

for date_entered in dates_entered:
	print(date_entered)