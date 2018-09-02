# choose a category
# then choose a number of states to drill in that category

# copied from github and altered

def capitals_nicknames_years(question):
	while True:
		reply = str(raw_input(question+' (a - capitals, b - nicknames, c - years founded): ')).lower().strip()
		if reply not in ['a', 'b', 'c']:
			print("invalid choice")
		else:
			if reply == 'a':
				print("you selected %s - capitals") % (reply)
			elif reply == 'b':
				print("you selected %s - nicknames") % (reply)
			elif reply == 'c':
				print("you selected %s - years founded") % (reply)
			break
			
capitals_nicknames_years("Would you like to drill")