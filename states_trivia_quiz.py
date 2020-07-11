"""Quiz game based on US states trivia."""

import functions
import pyinputplus as pyip

categories = {
    1: 'Capitals',
    2: 'Nicknames',
    3: 'Years Founded',
    4: 'Order Admitted',
    }

print('\nChoose a category to drill.')
for num, category in categories.items():
    print(num, category)

user_input = pyip.inputInt('> ', min=1, max=len(categories))
CATEGORY_CHOICE = functions.switch_case(categories, user_input)
print(f'\nYou chose {CATEGORY_CHOICE}')

QUESTION = (f'How many states would you like to drill in that category?' \
            f' (select an integer between 1 and {len(functions.STATES)})\n> ')
functions.SEE_THE_ANSWER = ('Sorry, that\'s incorrect. Would you like to see '
                            'the correct answer?')

functions.NUM_STATES = pyip.inputInt(QUESTION, min=1, max=len(functions.STATES))

if CATEGORY_CHOICE == 'Capitals':
    functions.quiz(functions.capital, functions.CAPITALS)
elif CATEGORY_CHOICE == 'Nicknames':
    functions.quiz(functions.nickname, functions.NICKNAMES)
elif CATEGORY_CHOICE == 'Years Founded':
    functions.quiz(functions.year_founded, functions.YEARS_FOUNDED)
else:
    functions.quiz(functions.order, functions.ORDERS)

print('\n')
