# Functions are the building blocks of programming 
# Defining functions in python,
# def keyword + name + paramater: 
#   return statement + return value
# def fahr_to_kelvin(temp)
#   return((temp - 32) * (5/9)) + 273.15

# A minimal function (stub up \ placeholder)
# def first_function():
#     pass
# result = first_function()
# print(result)

# differences in Python & JS Functions
# Python functions are defined using the def keyword and the
# functions cannot be assigned to variables
# Python uses teh inline function (lambda), they're very much like
# arrow functions.
# lambda functions implicitly return a single expression result
# lambda function can be assigned to a variable, example:
# nums = [1, 3, 2, 6, 5]
# odds = list( filter(lambda num: num % 2, nums) )

# Python doesn't hoist functions!
# You cannot call functions before it's declared

# Calling functons
# def add(a, b):
#   return a + b

# def sub(a, b):
#   return a - b

# def compute(a, b, op):
#   return op(a, b)

# print( compute(1, 2, add) )

# *** Python requires that the correct number of arguments are provided
# *** when calling a function
# example:

# def add(a, b):
#   return a + b
# add() <- need to pass in only two arguments to run the function

# Generates the following error:
# TypeError: add() missing 2 required positional arguments:

# Using the * specifier in a paramter list allows us to pass in a
# varying number of arugments into a function:(Just like (...nums) in JS)
# def f(*args):
#   print( type(args) )
#   for arg in args:
#     print(arg)

# f(1, 2, 'SEI')

# Always use the *argsparameter after any required positional parameters. For example:
# def dev_skills(dev_name, *args):
#   dev = {'name': dev_name, 'skills': []}
#   for skill in args:
#     dev['skills'].append(skill)
#   return dev

# print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))
# -> {'name': 'Alex', 'skills': ['HTML', 'CSS', 'JavaScript', 'Python']}

# EVERYTHING IN dev_skills after the 'dev_name' ('Alex') is passed 
# into the function as *args

# def dev_skills(dev_name, **kwargs):
#   dev = {'name': dev_name, 'skills': {}}
#   # unpacking the tuples returned by the items function
#   for skill, rating in kwargs.items():
#     dev['skills'][skill] = rating
#   return dev

# print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=2))

# The dev_name is the positional argument and the **kwargs are
# the key:value (dictionaries) pairs passed in as an argument

# We can even combine *args & **kwargs

# def arg_demo(pos1, pos2, *args, **kwargs):
#   print(f'Positional params: {pos1}, {pos2}')
#   print('*args:')
#   for arg in args:
#     print(' ', arg)
#   print('**kwargs:')
#   for keyword, value in kwargs.items():
#     print(f'  {keyword}: {value}')

# arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')

