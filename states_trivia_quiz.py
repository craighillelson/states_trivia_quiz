"""__doc__"""

# imports
import csv
import random
from datetime import datetime
import time

RTN = lambda: '\n'

def quiz(item, lst):
    # define variables
    """ quiz user """
    print CATEGORY_HEADER
    print RTN()
    correct = 0
    incorrect = 0
    # for the number of states the user specified to drill, generate an equal number of
    # random numbers less than 50
    for j in i:
        print RTN()
        state = STATES[j]
        state_formatted = "%s " % (state)
        item = lst[j]
        user_answer = raw_input(state_formatted)
        # test the user's answer and respond
        if user_answer == item:
            print "Correct. Good job!\n"
            correct = correct + 1
            CORRECTS.append(state)
        else:
            incorrect = incorrect + 1
            INCORRECTS.append(state)
            while True:
                see_the_answer_response = str(raw_input(SEE_THE_ANSWER+
                                                        ' (y or n): ')).lower().strip()
                if see_the_answer_response not in ['y', 'n']:
                    print "invalid choice"
                # give user the correct answer
                elif see_the_answer_response == 'y':
                    print "The correct answer is %s" % (lst[j])
                    break
                else:
                    break

    # calculate and format percentage correct
    percentage_correct = float(correct) / float(USER_CHOICE)
    percentage_formatted = "{0:.0%}".format(percentage_correct)
    print("Results: %s correct %s incorrect. %s\n") % (correct, incorrect, percentage_formatted)
    # update user with their results. if user got any wrong, write the states missed to a text file
    current_timestamp = time.time()
    datetime_ts = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d_%H-%M')
    datetime_ts = "%s.txt" % (datetime_ts)
    with open(datetime_ts, 'w') as results:
        if incorrect > 0:
            results.write("Category: "+ QUIZ_CATEGORY+ "\n\n")
            results.write("States to Review"+ "\n")
            print "States to brush up on:"
            for states_missed in INCORRECTS:
                results.write(states_missed+ "\n")
                print states_missed
            print RTN()
            print "Check %s to see where you can improve." % (datetime_ts)
            print RTN()
        else:
            results.write("Great job!!! 100%")
            print "Great job!!! 100%"
            print RTN()

# define lists to be populated later
STATES = []
CAPITALS = []
NICKNAMES = []
YEARS_FOUNDED = []
ORDERS = []
CORRECTS = []
INCORRECTS = []

# import csv
with open('states_trivia.csv') as f:
    F_CSV = csv.DictReader(f)
    for row in F_CSV:
        capital = row['capital']
        nickname = row['nickname']
        year_founded = row['year founded']
        order = row['order']
        STATES.append(row['state'])
        CAPITALS.append(row['capital'])
        NICKNAMES.append(row['nickname'])
        YEARS_FOUNDED.append(row['year founded'])
        ORDERS.append(row['order'])

# get length of the list of states
NUMBER_OF_STATES = len(STATES)

# define questions
CATEGORY = """Would you like to drill a - capitals, b - nicknames, c - years founded,
or d - order admitted? """
QUESTION = """How many states would you like to drill in that category?
(select an integer between 1 and %s) """ % (NUMBER_OF_STATES)
SEE_THE_ANSWER = "Sorry, that's incorrect. Would you like to see the correct answer?"

# define responses
TOO_MANY = "Please select an integer less than %s " % (NUMBER_OF_STATES)
NOT_AN_INTEGER = "That won't work. Please enter an integer between 1 and 50. "

# prompt user to select a category
while True:
    CATEGORY_CHOICE = str(raw_input(CATEGORY)).lower().strip()
    if CATEGORY_CHOICE not in ['a', 'b', 'c', 'd']:
        print "invalid choice"
    else:
        if CATEGORY_CHOICE == 'a':
            print "you selected %s - capitals" % (CATEGORY_CHOICE)
            CATEGORY_HEADER = "Type the capital of each state."
            QUIZ_CATEGORY = "Capitals"
        elif CATEGORY_CHOICE == 'b':
            print "you selected %s - nicknames" % (CATEGORY_CHOICE)
            CATEGORY_HEADER = "Type the nickname of each state."
            QUIZ_CATEGORY = "Nicknames"
        elif CATEGORY_CHOICE == 'c':
            print "you selected %s - years founded" % (CATEGORY_CHOICE)
            CATEGORY_HEADER = "Type the year each state joined the union."
            QUIZ_CATEGORY = "Year Founded"
        else:
            print "you selected %s - order admitted" % (CATEGORY_CHOICE)
            CATEGORY_HEADER = "Type the order in which each state was admitted to the union."
            QUIZ_CATEGORY = "Order Admitted"
        break

# prompt user to select how many states they'd like to drill
while True:
    try:
        USER_CHOICE = int(raw_input(QUESTION))
    except ValueError:
        print "Please enter an integer."
        continue
    if USER_CHOICE > NUMBER_OF_STATES:
        print "Please enter an integer between 1 and 50."
    else:
        break

i = random.sample(range(NUMBER_OF_STATES), int(USER_CHOICE))

# prompt user
if CATEGORY_CHOICE == 'a':
    quiz(capital, CAPITALS)
elif CATEGORY_CHOICE == 'b':
    quiz(nickname, NICKNAMES)
elif CATEGORY_CHOICE == 'c':
    quiz(year_founded, YEARS_FOUNDED)
else:
    quiz(order, ORDERS)
