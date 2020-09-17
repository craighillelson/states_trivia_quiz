"""Functions."""

import csv
import pyinputplus as pyip
import random
import time
from datetime import datetime

with open("states_trivia.csv", "r") as states_data:
    STATES = []
    CAPITALS = []
    NICKNAMES = []
    YEARS_FOUNDED = []
    ORDERS = []
    CORRECTS = []
    INCORRECTS = []
    F_CSV = csv.DictReader(states_data)
    for row in F_CSV:
        capital = row["capital"]
        nickname = row["nickname"]
        year_founded = row["year founded"]
        order = row["order"]
        STATES.append(row["state"])
        CAPITALS.append(row["capital"])
        NICKNAMES.append(row["nickname"])
        YEARS_FOUNDED.append(row["year founded"])
        ORDERS.append(row["order"])


def calculate_percentage():
    """Calculate perecentage answered correctly."""
    percentage_correct = float(len(CORRECTS)) / float(NUM_STATES)
    return '{0:.0%}'.format(percentage_correct)


def concat_results_file_name():
    """Concatenate results file name."""
    timestamp = time.time()
    datetime_ts = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d_%H-%M")
    return "%s.txt" % (datetime_ts)


def output_and_write_results(sing_or_plural, text_file):
    """Output results to the screen and write them to a text file."""
    text_file.write(f"{sing_or_plural} to Review\n")
    print(f"{sing_or_plural} to brush up on:")
    for states_missed in INCORRECTS:
        text_file.write(f"{states_missed}\n")
        print(states_missed)


def output_overall_results(lst1, lst2, perc):
    """Outputs user's results."""
    print(f"\nResults: {len(lst1)} correct {len(lst2)} incorrect."
          f" {perc}\n")


def prompt_user_for_category(dct):
    """Output options and prompt user to select a category."""
    print("\nChoose a category to drill.")
    for num, category in dct.items():
        print(num, category)
    return pyip.inputInt("> ", min=1, max=len(dct))


def process_user_choice(dct, a):
    """Return the user's category choice."""
    return switch_case(dct, a)


def prompt_user_for_number_states():
    """Prompt user for number of states they'd like to drill."""
    HOW_MANY = (f"How many states would you like to drill in that category?" \
                f" (select an integer between 1 and " \
                f"{len(STATES)})\n> ")
    return pyip.inputInt(HOW_MANY, min=1, max=len(STATES))


def quiz(state, fact):
    """Quiz user."""
    random_integers = random.sample(range(len(STATES)), int(NUM_STATES))
    for number in random_integers:
        state = STATES[number]
        state_fact = fact[number]
        user_answer = input(f"\n{state}\n> ")
        if user_answer == state_fact:
            print("Correct. Good job!")
            CORRECTS.append(state)
        else:
            INCORRECTS.append(state)
            while True:
                see_the_answer_response = pyip.inputYesNo("Would you like to "
                                                          "see the correct "
                                                          "answer?\n> ")
                if see_the_answer_response == "yes":
                    print(f"The correct answer is {fact[number]}")
                    break
                else:
                    break

    percentage_formatted = calculate_percentage()
    output_overall_results(CORRECTS, INCORRECTS, percentage_formatted)

    results_file = concat_results_file_name()
    with open(results_file, 'w') as results:
        if INCORRECTS:
            if len(INCORRECTS) > 1:
                output_and_write_results("States", results)
            else:
                output_and_write_results("State", results)
            print(f"\nCheck {results_file} to see where you can improve.")
        else:
            one_hundred = "Great job!!! 100%\n"
            results.write(one_hundred)
            print(one_hundred)
            print("You answered the following correctly:")
            for us_state in CORRECTS:
                print(us_state)
                results.write(f'{us_state}\n')


def switch_case(dct, argument):
    """Switch case statement."""
    dct
    return dct.get(argument, "nothing")
