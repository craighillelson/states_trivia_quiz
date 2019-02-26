""" __doc__ """

# imports
import csv
import random
from datetime import datetime
import time

# define lambda
RTN = lambda: "\n"


# def function
def quiz(state, fact):
    """ quiz user """
    # define variables
    print(CATEGORY_HEADER)
    print(RTN())
    correct = 0
    incorrect = 0
    # for the number of states the user specified to drill,
    # generate an equal number of random numbers less than 50
    for j in i:
        print(RTN())
        state = STATES[j]
        state_fact = fact[j]
        user_answer = input(f"{state} ")
        # test the user's answer and respond
        if user_answer == state_fact:
            print("Correct. Good job!\n")
            correct = correct + 1
            CORRECTS.append(state)
        else:
            incorrect = incorrect + 1
            INCORRECTS.append(state)
            while True:
                see_the_answer_response = str(input(
                    SEE_THE_ANSWER+' (y or n): ')).lower().strip()
                if see_the_answer_response not in ['y', 'n']:
                    print("invalid choice")
                # give user the correct answer
                elif see_the_answer_response == 'y':
                    print(f"The correct answer is {fact[j]}")
                    break
                else:
                    break

    # calculate and format percentage correct
    percentage_correct = float(correct) / float(USER_CHOICE)
    percentage_formatted = "{0:.0%}".format(percentage_correct)
    print(f"Results: {correct} correct {incorrect} incorrect." +
          f" {percentage_formatted}\n")

    # update user with their results. if user got any wrong,
    # write the states missed to a text file
    timestamp = time.time()
    datetime_ts = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M')
    datetime_ts = "%s.txt" % (datetime_ts)
    with open(datetime_ts, 'w') as results:
        if incorrect:
            results.write("Category: "+ QUIZ_CATEGORY+ "\n\n")
            results.write("States to Review"+ "\n")
            print("States to brush up on:")
            for states_missed in INCORRECTS:
                results.write(states_missed+ "\n")
                print(states_missed)
            print(RTN())
            print(f"Check {datetime_ts} to see where you can improve.")
            print(RTN())
        else:
            results.write("Great job!!! 100%")
            print("Great job!!! 100%")
            print("You answered the following correctly:")
            for us_state in CORRECTS:
                print(us_state)
            print(RTN())


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
CATEGORY = ("Would you like to drill a - capitals, b - nicknames," +
            "c - years founded, or d - order admitted? ")
QUESTION = (f"How many states would you like to drill in that category?" +
            f"select an integer between 1 and {NUMBER_OF_STATES}) ")
SEE_THE_ANSWER = ("Sorry, that's incorrect. Would you like to see the correct" +
                  "answer?")

# define responses
TOO_MANY = f"Please select an integer less than {NUMBER_OF_STATES} "
NOT_AN_INTEGER = "That won't work. Please enter an integer between 1 and 50. "

# prompt user to select a category
while True:
    CATEGORY_CHOICE = str(input(CATEGORY)).lower().strip()
    if CATEGORY_CHOICE not in ['a', 'b', 'c', 'd']:
        print("invalid choice")
    else:
        if CATEGORY_CHOICE == 'a':
            print(f"you selected {CATEGORY_CHOICE} - capitals")
            CATEGORY_HEADER = "Type the capital of each state."
            QUIZ_CATEGORY = "Capitals"
        elif CATEGORY_CHOICE == 'b':
            print(f"you selected {CATEGORY_CHOICE} - nicknames")
            CATEGORY_HEADER = "Type the nickname of each state."
            QUIZ_CATEGORY = "Nicknames"
        elif CATEGORY_CHOICE == 'c':
            print(f"you selected {CATEGORY_CHOICE} - years founded")
            CATEGORY_HEADER = "Type the year each state joined the union."
            QUIZ_CATEGORY = "Year Founded"
        else:
            print(f"you selected {CATEGORY_CHOICE} - order admitted")
            CATEGORY_HEADER = """Type the order in which each state was admitted
                                 to the union."""
            QUIZ_CATEGORY = "Order Admitted"
        break

# prompt user to select how many states they'd like to drill
while True:
    try:
        USER_CHOICE = int(input(QUESTION))
    except ValueError:
        print("Please enter an integer.")
        continue
    if USER_CHOICE > NUMBER_OF_STATES:
        print("Please enter an integer between 1 and 50.")
    else:
        break

# set i equal to a list of random numbers where the number of items in the list
# is the number selected by the user and the range is the number of states
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
