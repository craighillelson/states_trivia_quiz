"""Command line quiz game based on states trivia."""

import csv
import random
import time
from datetime import datetime
import pyinputplus as pyip


def build_file_name(v):
    datetime_string = build_timestamp_string()
    if v == "order admitted":
        v = "order_admitted"
    elif v == "years founded":
        v = "years_founded"
    else:
        pass

    return v + "_" + datetime_string + ".txt"


def build_list_of_state_prompts(lst2, lst3):
    lst1 = []
    for random_number in lst2:
        lst1.append(lst3[random_number])

    return lst1


def build_quiz(category):
    print(f"\n> {category}".title().format(category))
    states_facts = build_states_facts_dictionary()
    states = get_states(states_facts)
    number_of_quiz_items = prompt_user_for_NUMBER_OF_STATES()
    list_of_random_numbers = \
    generate_list_of_random_numbers(number_of_quiz_items)
    state_prompts = build_list_of_state_prompts(list_of_random_numbers, states)

    category_map = {
        'capitals': ["What is the capital of {}", 0],
        'nicknames': ["What is {}'s nickname", 1],
        'years founded': ["What year was {} founded", 2],
        'order admitted': ["{} was admitted as what number state", 3]
        }

    lst1, lst2 = \
    compile_lists_of_correct_and_incorrect_answers(state_prompts,
                                                   category_map, category,
                                                   states_facts)

    output_results(category, lst1, lst2)
    file_name = build_file_name(category)
    write_results_to_text_file(file_name, lst1, lst2)


def build_states_facts_dictionary():
    dct = {}
    with open("states_trivia.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dct[row["state"]] = [row["capital"], row["nickname"],
                                 row["year_founded"], row["order"]]

    return dct


def build_timestamp_string():
    timestamp = time.time()
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M-%S')


def compile_lists_of_correct_and_incorrect_answers(lst3, dct1, v, dct2):
    lst1 = []
    lst2 = []
    for state in lst3:
        prompt = f"\n{dct1[v][0]}?"
        print(prompt.format(state))
        answer = dct2[state][dct1[v][1]]
        user_response = input("> ")
        if user_response == answer:
            print("correct")
            lst1.append(state)
        else:
            print("incorrect")
            lst2.append(state)
            print(answer)

    return lst1, lst2


def generate_list_of_random_numbers(number):
    return random.sample(range(1, NUMBER_OF_STATES), number)


def get_number_of_states():
    states_facts = build_states_facts_dictionary()
    return len(states_facts)


def get_states(dct):
    return list(dct.keys())


def main_menu():
    categories = {
        1: 'capitals',
        2: 'nicknames',
        3: 'years founded',
        4: 'order admitted',
        }

    while True:
        print("\nPlease select an option below or nothing to exit\n")
        for num, option in categories.items():
            print(f"{num}. {option}".title())
        user_choice = pyip.inputInt("> ", min=1, max=len(categories),
                                    blank=True)
        if user_choice != "":
            selected = categories[user_choice]
            build_quiz(selected)
        else:
            break


def output_results(v, lst1, lst2):
    print(f"\n{v}".title())
    output_as_singular_or_plural("correct answers", "correct answer", lst1)
    output_as_singular_or_plural("incorrect answers", "incorrect answer",lst2)


def prompt_user_for_NUMBER_OF_STATES():
    states_facts = build_states_facts_dictionary()
    NUMBER_OF_STATES = len(states_facts)
    how_many = (f"\nHow many states would you like to drill in that category?" \
                f" (select an integer between 1 and " \
                f"{NUMBER_OF_STATES})\n> ")
    return pyip.inputInt(how_many, min=1, max=NUMBER_OF_STATES)


def output_as_singular_or_plural(plural_header, singular_header, lst):
    if lst:
        if len(lst) > 1:
            print(f"\n{plural_header}".title())
            for answer in lst:
                print(answer)
        else:
            print(f"\n{singular_header}".title())
            for answer in lst:
                print(answer)


def write_results_to_text_file(file_name, lst1, lst2):
    file = open(file_name, "w")

    file.write("correct answers\n")
    for item in lst1:
        file.write(f"{item}\n")

    file.write("\nincorrect answers\n")
    for item in lst2:
        file.write(f"{item}\n")


NUMBER_OF_STATES = get_number_of_states()
main_menu()
