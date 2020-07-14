"""Quiz game based on US states trivia."""

import functions
import pyinputplus as pyip

categories = {
    1: 'Capitals',
    2: 'Nicknames',
    3: 'Years Founded',
    4: 'Order Admitted',
    }

user_input = functions.prompt_user_for_category(categories)
CATEGORY_CHOICE = functions.process_user_choice(categories, user_input)
print(f'\nYou chose {CATEGORY_CHOICE}')

functions.NUM_STATES = functions.prompt_user_for_number_states()

if CATEGORY_CHOICE == 'Capitals':
    functions.quiz(functions.capital, functions.CAPITALS)
elif CATEGORY_CHOICE == 'Nicknames':
    functions.quiz(functions.nickname, functions.NICKNAMES)
elif CATEGORY_CHOICE == 'Years Founded':
    functions.quiz(functions.year_founded, functions.YEARS_FOUNDED)
else:
    functions.quiz(functions.order, functions.ORDERS)

print('\n')
