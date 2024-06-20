# qn.1
import random
import string

random_user_id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(6)])
print(random_user_id)


# qn2
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

#qn3

from math import pi
r = float(input("Input the radius of the circle : "))
area = pi * r ** 2
print("The area of the circle with radius " + str(r) + " is: " + str(area))


#qn 4

# Temperature in celsius degree
celsius = 47

# Converting the temperature to
# fehrenheit using the formula
fahrenheit = (celsius * 1.8) + 32

# printing the result
print('%.2f Celsius is equivalent to: %.2f Fahrenheit'
	% (celsius, fahrenheit))



#qn 5
month = input("Input the month (e.g. January, February etc.): ")


if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'fall'

print("Season is",season)


#qn6

def print_list(lst):
    for item in lst:
        print(item)


#Qn 7: 

# reverse_list.py
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))  # ["C", "B", "A"]


#Qn8: Function to capitalize list items

# capitalize_list_items.py
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]


#Qn9: Function to add an item to a list

# add_item.py
def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))  # [2, 3, 7, 9, 5]


#Qn 10: Function to sum numbers in a range

# sum_of_numbers.py
def sum_of_numbers(n):
    return sum(range(1, n + 1))

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

#Qn11: Function to sum odd numbers in a range

# sum_of_odds.py
def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

#Qn 12: Function to sum even numbers in a range
# sum_of_evens.py
def sum_of_evens(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)

#Qn13: Function to count evens and odds in a range

# evens_and_odds.py
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

print(evens_and_odds(100))

#Qn14: Function to check if a number is prime
#is_prime.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Qn15: Function to check if all items in the list are unique
# all_unique.py
def all_unique(lst):
    return len(lst) == len(set(lst))

#Qn16: Function to check if all items in the list are of the same data type
# all_same_type.py
def all_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)

#Qn 17: Loop to print a triangle pattern

# triangle_pattern.py
for i in range(1, 8):
    print('#' * i)

#Qn18: Loop to print a multiplication table

# multiplication_table.py
for i in range(11):
    print(f"{i} x {i} = {i * i}")

#Qn19: Loop to print even numbers from 0 to 100

# even_numbers.py
for i in range(0, 101, 2):
    print(i)

#Qn 20: Loop to print odd numbers from 0 to 100

# odd_numbers.py
for i in range(1, 101, 2):
    print(i)

#Qn21: Function to get user input and provide feedback based on age
# check_age.py
def check_age():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are old enough to drive.")
    else:
        print(f"You need {18 - age} more years to learn to drive.")

#Qn22: Function to grade students based on scores
# grade_student.py
def grade_student(score):
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score < 80:
        return 'B'
    elif 60 <= score < 70:
        return 'C'
    elif 50 <= score < 60:
        return 'D'
    else:
        return 'F'
    
#Qn23: Create an empty dictionary called dog

# dog_dictionary.py
dog = {}

#Qn24: Add properties to the dog dictionary

# dog_properties.py
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

#Qn25: Create a student dictionary and add keys

# student_dictionary.py
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

#Qn26: Get the length of the student dictionary

# student_length.py
len(student)

#Qn 27: Get the value of skills and check the data type

# check_skills.py
skills = student['skills']
type(skills)

#Qn28: Modify the skills values by adding one or two skills

# add_skills.py
student['skills'].append('HTML')

#Qn29: Get the dictionary keys as a list

# dictionary_keys.py
keys = list(student.keys())

#Qn30: Get the dictionary values as a list

# dictionary_values.py
values = list(student.values())

#Qn31: Create an empty tuple

# empty_tuple.py
empty_tuple = ()

#Qn32: Create a tuple containing names of your siblings

# siblings_tuple.py
brothers = ('John', 'Mike')
sisters = ('Anna', 'Emily')



#Qn33: Join brothers and sisters tuples and assign to siblings

# siblings.py
siblings = brothers + sisters


#Qn34: Modify the siblings tuple and add the name of your parents

# family_members.py
family_members = siblings + ('Father', 'Mother')



