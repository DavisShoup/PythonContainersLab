# Let's discuss Dictionaries

# student = {
#     'name': 'Wilma',
#     'course': 'SEIR',
#     'current_week': 10
# }

# print(student)
# print(type(student))

# Let's go over how to add key:value pairs to a dictionary

# we do not use dot notation for getting or setting values

# student['name'] = 'Betty'
# print(student['name'])

#What happens if we try to access a value that doesn't exist

# print(student['location'])

# We use the get() methond

# print(student.get('location'))

# the .get() method permits us to provide a default value as a second argument
# print(student.get('location', 'Dallas, Texas'))

# if student['name'] == 'Wilma':
#     print('its Wilma')
# else:
#     print('Not Wilma')

# Add values

# student['location'] = 'Los Angeles, CA'

# Modify values
# student['course'] = 'SEIR Flex'

# Deleting values

# del student['location']

# print(student)

# print the number of itmes inside a dictionary

# print(len(student))

# iterate over the items in a dictionary

# This works but it's an anti-pattern
# for key in student:
#     print(student[key])

# preferred way - using dictionary view object

# print(student.items())

# dict_items([('name', 'Wilma'), ('course', 'SEIR'), ('current_week', 10)])
# touple unpacking
# for key, value in student.items():
#     print(key, value)



# Define a Python dictionary named where_my_things_are with keys containing a few items; where the things you have, and the valueis of the location you keep those things.
# Write a forloop that iterates over the items in the dictionary and prints each one as My [thing] is kept [location].

# where_my_thing_are = {
#     'phone': 'bed',
#     'keyboard': 'desk',
#     'coffee': 'kitchen'
# }

# for item, location in where_my_thing_are.items():
#     print(f"My {item} is kept at my {location}.")

# Let's practice with lists

# colors = ['red', 'white', 'blue']

# print(type(colors))
# print(len(colors))

# They are oredered collections
# They are also considered sequence types
# They are mutable

# Accessing values in a list
# last_color = colors[2]
# some_color = colors[2-1]
# # accessing the last value
# last_color_2 = colors[-1]
# assigning values in a list
# colors[-1] = 'orange'
# adding items to a list
# colors.append('purple') # .append() only pushes 1 item into a list
# colors.extend(['black', 'grey']) # .extend() pushes multiple items into a list
# inserting items, .insert() will push an item into a specific location in a list
# colors.insert(0, 'yellow')
# deleting/removing items in a list
# colors.pop()
# .remove() - not the preferred way to delete, can cause an error if you enter an item that doesn't exist
# colors.remove('red')
# del will remove the item from memory
# del colors[1]
# complete remove an entire list
# colors.clear()

# Lists: Iternation
# for statement - good for when we just need the items
# for color in colors:
#     print(color)
# for statment with the enumerate method, a way to view the index of an item in a list
# for index, color in enumerate(colors):
#     print(index, color)

# what enumerate is doing, it's unpacking a touple like this, [(0, 'red'), (1, 'white'), ....]

# List comprehensions

# nums = list(range(1, 101))

# Filtering for odds using a for statement 
# for num in nums:
#     if num % 2 == 1:
#         odds.append(num)


# breakdown below: (n) = variable, (for n in nums) = the for loop, (if n % 2 == 1) = the conditional
# odds = [n for n in nums if n % 2 == 1]

# print(odds)

# Tuples

# Tuples are very similar to lists, 
# Tuples are instances of the tuple class
# Tuples are immutable - we cannot make changes to them
# Tuples take up less space in memory because they have fewer methods
# we iterate over a tuple way faster than a list

# colors = ('red', 'white', 'blue')

person = ('name', 'sally')


# colors[0] = 'orange' we cannot perform item assignment because typles are immutable

# for item in person:
#     print(item)

# for index, item in enumerate(person):
#     print(index, item)

# Tuple unpacking
# name_key, name = person

# print(name_key, name)

# Sequences and the slice operator

# print("hello"[:-1])

# print(person[1:])

# my_list = list(range(1, 100))[0:50:2]

# print(my_list)




