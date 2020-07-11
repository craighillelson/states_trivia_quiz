"""Functions."""

import csv
import pyinputplus as pyip
import random
import time
from datetime import datetime

STATES = []
CAPITALS = []
NICKNAMES = []
YEARS_FOUNDED = []
ORDERS = []
CORRECTS = []
INCORRECTS = []

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


def calculate_percentage():
    """Calculate perecentage answered correctly."""
    percentage_correct = float(len(CORRECTS)) / float(USER_CHOICE)
    return '{0:.0%}'.format(percentage_correct)


def concat_results_file_name():
    """Concatenate results file name."""
    timestamp = time.time()
    datetime_ts = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M')
    return '%s.txt' % (datetime_ts)


def output_and_write_results(sing_or_plural, a):
    """Output results to the screen and write them to a text file. """
    a.write(f'{sing_or_plural} to Review\n')
    print(f'{sing_or_plural} to brush up on:')
    for states_missed in INCORRECTS:
        a.write(f'{states_missed}\n')
        print(states_missed)


def quiz(state, fact):
    """Quiz user."""
    random_integers = random.sample(range(len(STATES)), int(USER_CHOICE))
    for number in random_integers:
        state = STATES[number]
        state_fact = fact[number]
        user_answer = input(f'{state}\n> ')
        # test the user's answer and respond
        if user_answer == state_fact:
            print('Correct. Good job!\n')
            CORRECTS.append(state)
        else:
            INCORRECTS.append(state)
            while True:
                see_the_answer_response = pyip.inputYesNo('Would you like to '
                                                          'see the correct '
                                                          'answer?\n> ')
                if see_the_answer_response == 'yes':
                    print(f'The correct answer is {fact[number]}\n')
                    break
                else:
                    break

    percentage_formatted = calculate_percentage()
    print(f'Results: {len(CORRECTS)} correct {len(INCORRECTS)} incorrect.' \
          f' {percentage_formatted}\n')

    results_file = concat_results_file_name()
    with open(results_file, 'w') as results:
        if INCORRECTS:
            # results.write(f'Category: {QUIZ_CATEGORY}\n\n')
            if len(INCORRECTS) > 1:
                output_and_write_results('States', results)
            else:
                output_and_write_results('State', results)
            print(f'\nCheck {results_file} to see where you can improve.')
        else:
            results.write('Great job!!! 100%')
            print('Great job!!! 100%\n')
            print('You answered the following correctly:')
            for us_state in CORRECTS:
                print(us_state)
