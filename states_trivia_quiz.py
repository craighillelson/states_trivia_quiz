"""Quiz game based on US states trivia."""

# imports
import csv
import random
from datetime import datetime
import time

'''
def switch_case(argument):
    """ switch case statement """
    switcher = {
        "a": ["capital", "CAPITALS"],
        "b": ["nickname", "NICKNAMES"],
        "c": ["year_founded", "YEARS_FOUNDED"],
        "d": ["order", "ORDERS"],
        }
    return switcher.get(argument, "nothing")
'''


# def function
def quiz(state, fact):
    """Quiz user."""
    print(f"{CATEGORY_HEADER}\n")
    for number in random_integers:
        state = STATES[number]
        state_fact = fact[number]
        user_answer = input(f"{state} ")
        # test the user's answer and respond
        if user_answer == state_fact:
            print("Correct. Good job!\n")
            CORRECTS.append(state)
        else:
            INCORRECTS.append(state)
            while True:
                see_the_answer_response = str(input(
                    SEE_THE_ANSWER+" (y or n): ")).lower().strip()
                if see_the_answer_response not in ["y", "n"]:
                    print("invalid choice")
                # give user the correct answer
                elif see_the_answer_response == 'y':
                    print(f"The correct answer is {fact[number]}\n")
                    break
                else:
                    break

    # calculate and format percentage correct
    percentage_correct = float(len(CORRECTS)) / float(USER_CHOICE)
    percentage_formatted = "{0:.0%}".format(percentage_correct)
    print(f"Results: {len(CORRECTS)} correct {len(INCORRECTS)} incorrect." \
          f" {percentage_formatted}\n")

    # update user with their results. if user got any wrong,
    # write the states missed to a text file
    timestamp = time.time()
    datetime_ts = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M')
    datetime_ts = "%s.txt" % (datetime_ts)
    with open(datetime_ts, 'w') as results:
        if INCORRECTS:
            results.write(f"Category: {QUIZ_CATEGORY}\n\n")
            results.write("States to Review\n")
            print("States to brush up on:")
            for states_missed in INCORRECTS:
                results.write(f"{states_missed}\n")
                print(states_missed)
            print("\n")
            print(f"Check {datetime_ts} to see where you can improve.")
        else:
            results.write("Great job!!! 100%")
            print("Great job!!! 100%\n")
            print("You answered the following correctly:")
            for us_state in CORRECTS:
                print(us_state)


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

# define questions
CATEGORY = ("\nWould you like to drill?\n\na - capitals\nb - nicknames\n"\
            "c - years founded\nd - order admitted\n\n")
QUESTION = (f"How many states would you like to drill in that category?" \
            f" (select an integer between 1 and {len(STATES)})")
SEE_THE_ANSWER = ("Sorry, that's incorrect. Would you like to see the correct" \
                  "answer?")

# define responses
TOO_MANY = f"Please select an integer less than {len(STATES)} "
NOT_AN_INTEGER = f"That won't work. Please enter an integer between 1 and "\
                 f"{len(STATES)}. "

# prompt user to select a category
while True:
    CATEGORY_CHOICE = str(input(CATEGORY)).lower().strip()
    if CATEGORY_CHOICE not in ['a', 'b', 'c', 'd']:
        print("invalid choice")
    else:
        # restructure as a switch case statement
        if CATEGORY_CHOICE == 'a':
            print(f"you selected {CATEGORY_CHOICE} - capitals\n")
            CATEGORY_HEADER = "Type the capital of each state."
            QUIZ_CATEGORY = "Capitals"
        elif CATEGORY_CHOICE == 'b':
            print(f"you selected {CATEGORY_CHOICE} - nicknames\n")
            CATEGORY_HEADER = "Type the nickname of each state."
            QUIZ_CATEGORY = "Nicknames"
        elif CATEGORY_CHOICE == 'c':
            print(f"you selected {CATEGORY_CHOICE} - years founded\n")
            CATEGORY_HEADER = "Type the year each state joined the union."
            QUIZ_CATEGORY = "Year Founded"
        else:
            print(f"you selected {CATEGORY_CHOICE} - order admitted\n")
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
    if USER_CHOICE > len(STATES):
        print("Please enter an integer between 1 and 50.")
    else:
        break

# set i equal to a list of random numbers where the number of items in the list
# is the number selected by the user and the range is the number of states
random_integers = random.sample(range(len(STATES)), int(USER_CHOICE))

# prompt user
if CATEGORY_CHOICE == 'a':
    quiz(capital, CAPITALS)
elif CATEGORY_CHOICE == 'b':
    quiz(nickname, NICKNAMES)
elif CATEGORY_CHOICE == 'c':
    quiz(year_founded, YEARS_FOUNDED)
else:
    quiz(order, ORDERS)

# switch_case(CATEGORY_CHOICE)

print("\n")
