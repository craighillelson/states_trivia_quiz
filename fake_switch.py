# copied from https://www.pydanny.com/why-doesnt-python-have-switch-case.html

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")

print(numbers_to_strings(0))
print(numbers_to_strings(1))
print(numbers_to_strings(2))
print(numbers_to_strings(3))