# Exercise 1
# Create a list named studentscontaining some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

# students = ['Alex', 'James', 'Amber']
# print(students[1])
# print(students[-1])

# Exercise 2
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

# foods = ('Pizza', 'Cheese', 'Banana')
# for food in foods:
#     print(f"{food} is a good food.")

# Exercise 3
# Using a forloop, print just the last two food strings from foods.

# for food in foods:
#     if food == foods[-1] or food == foods[-2]:
#         print(food)

# for food in foods[-3:]:
#     print(food)


# Exercise 4
# Create a dictionary named home_towncontaining the keys of city, stateand population.
# Print a string with this format:
# "I was born in city, state - population of population"

# home_town = {
#     'city': 'Atlanta',
#     'state': 'Georgia',
#     'population': '497,642'
# }

# city = home_town['city']
# state = home_town['state']
# population = home_town['population']

# print(f"I was born in {city}, {state}, with a population of {population}.")

# Exercise 5
# Iterate over the key: value pairs in home_townand print a string for each item, for example:
# 	"city = Arcadia"
# 	"state = California"
# 	"population = 58000"

# for key, value in home_town.items():
#     print(f"{key} = {value}")


# Exercise 6
# Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohortlist for each student name. Each dictionary should have this shape:
# {
# 	'student': 'Tina',
# 	'fav_food': 'Cheeseburger'
# }

# cohort = []
# for index, student in enumerate(students):
#     cohort.append({
#         'student': student,
#         'fav_food': foods[index]
#     })
# print(cohort)

# Exercise 7
# Using the list of studentsand list comprehension, assign to a variable named awesome_studentsa new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_studentsprinting out each string.

# awesome_students = [f'{student} is awesome!' for student in students]
# print(awesome_students)


# Exercise 8
# Using the tuple foodsand list comprehension within a forloop, print each food string that contains the letter a.

# for food in foods:
#     if 'a' in food:
#         print(food)