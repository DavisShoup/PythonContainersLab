# 1. Write a function named sum_to that accepts a single integer, n, 
# and returns the sum of the integers from 1 to n. For example:
# sum_to(6)  # returns 21
# sum_to(10) # returns 55

# def sum_to(n):
#     nums = range(1, n+1)
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum

# print(sum_to(10))

# 2. Write a function named largest that takes a list of numbers as 
# an argument and returns the largest number in that list.For example:
# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231

# def largest(nums):
#     x = 0
#     for num in nums:
#         x = num + x
#         if x > num:
#             return num

# print(largest([10, 20, 200, 1500]))


# 3. Write a function named occurances that takes two string arguments 
# as input and counts the number of occurances of the second string 
# inside the first string. For example:
# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

# def occurances(a, b):
#     match = 0
#     for letter_b in b:
#         for letter_a in a:
#             if(letter_a == letter_b):
#                 match += 1
#     return match

# print(occurances('flee floop', 'p'))

# 4. Write a function named product that takes an arbitrary number 
# of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args). For example:

# def product(*args):
#     product = 1
#     for num in args:
#         product *= num
#     return product

# print(product(5, 5, 5, 5))




