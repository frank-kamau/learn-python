import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required")
    cost_per_person = math.ceil(total / number_of_people)
    return cost_per_person

try:
    total_due = float(input('what is the total?  '))
    number_of_people = int(input('how many people?  '))
    amount_due = split_check(total_due, number_of_people)
except ValueError:
    print('That is not a valid value.  Please try again.')
else:


    print(f'Each person owes ksh{amount_due}')