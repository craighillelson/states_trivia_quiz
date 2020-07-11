"""Quiz game based on US states trivia."""

import functions
import pyinputplus as pyip

CATEGORY = ('\nWould you like to drill?\n\na - capitals\nb - nicknames\n'\
            'c - years founded\nd - order admitted\n\n> ')
QUESTION = (f'How many states would you like to drill in that category?' \
            f' (select an integer between 1 and {len(functions.STATES)})\n> ')
functions.SEE_THE_ANSWER = ('Sorry, that\'s incorrect. Would you like to see '
                            'the correct answer?')

while True:
    CATEGORY_CHOICE = str(input(CATEGORY)).lower().strip()
    if CATEGORY_CHOICE not in ['a', 'b', 'c', 'd']:
        print('invalid choice')
    else:
        # restructure as a switch case statement
        if CATEGORY_CHOICE == 'a':
            print(f'you selected {CATEGORY_CHOICE} - capitals\n')
            CATEGORY_HEADER = 'Type the capital of each state.'
            QUIZ_CATEGORY = 'Capitals'
        elif CATEGORY_CHOICE == 'b':
            print(f'you selected {CATEGORY_CHOICE} - nicknames\n')
            CATEGORY_HEADER = 'Type the nickname of each state.'
            QUIZ_CATEGORY = 'Nicknames'
        elif CATEGORY_CHOICE == 'c':
            print(f'you selected {CATEGORY_CHOICE} - years founded\n')
            CATEGORY_HEADER = 'Type the year each state joined the union.'
            QUIZ_CATEGORY = 'Year Founded'
        else:
            print(f'you selected {CATEGORY_CHOICE} - order admitted\n')
            CATEGORY_HEADER = '''Type the order in which each state was admitted
                                 to the union.'''
            QUIZ_CATEGORY = 'Order Admitted'
        break

while True:
    functions.USER_CHOICE = pyip.inputInt(QUESTION, min=1,
                                          max=len(functions.STATES))
    break

print(f'\n{CATEGORY_HEADER}')
if CATEGORY_CHOICE == 'a':
    functions.quiz(functions.capital, functions.CAPITALS)
elif CATEGORY_CHOICE == 'b':
    functions.quiz(functions.nickname, functions.NICKNAMES)
elif CATEGORY_CHOICE == 'c':
    functions.quiz(functions.year_founded, functions.YEARS_FOUNDED)
else:
    functions.quiz(functions.order, functions.ORDERS)

print('\n')
