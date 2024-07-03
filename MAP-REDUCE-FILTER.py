# Square all numbers in a list (task 1)

# def square(n):
#     return n**2

# my_list = [7,2,3,4,5,6,7,8,9]

# result = map(square,my_list)

# print(list(result))

# Convert all strings in a list to uppercase(task 2)

# from functools import reduce

# my_list= ["hello", "world", "python", "programming"]
# mapped_list = map(lambda x: x.upper(), my_list)
# that_list = filter(lambda x: isinstance(x, str), mapped_list)
# final_list = reduce(lambda x, y: x + [y], that_list, [])

# print(final_list)

# Add 10 to each number in a list(task 3)

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# mapped_list = map(lambda x: x + 10, numbers)
# the_list = filter(lambda x: isinstance(x, (int, float)), mapped_list)
# final_list = reduce(lambda x, y: x + [y], the_list, [])

# print(final_list)

# Double each number in a list(task 4)

# def double(n):
#     return n*2

# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# result = map(double,my_list)

# print(list(result))

# Capitalize the first letter of each string in a list(task 5)

# my_list = ["hello", "world", "python", "programming"]
# capitalized_list = list(map(lambda x: x.capitalize(), my_list))

# print(capitalized_list)

# Filter out even numbers from a list(task 6)

# def even(n):
#     return n%2==0
# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# result = filter(even,my_list)

# print(list(result))

# Filter out words shorter than 4 characters(task 7)

# from functools import reduce

# my_list = ["low", "word", "python", "programming", "is", "some"]
# result = reduce(lambda x, y: x + [y], filter(lambda x: len(x) <= 4, my_list), [])

# print(result)

# Filter out numbers greater than 10(task 8)

# from functools import reduce

# numbers = [3, 15, 7, 12, 9, 20]
# my_list = reduce(lambda x, y: x + [y], filter(lambda x: x >= 10, numbers), [])

# print(my_list)

# Filter out strings containing the letter 'a'(task 9)

# from functools import reduce

# my_list = ["air","water","fire","land","sky"]
# result = reduce(lambda x, y: x + [y], filter(lambda x: 'a' in x, my_list), [])

# print(result)

# Filter out numbers that are not divisible by 3(task 10)

# from functools import reduce

# numbers = [1, 3, 5, 9, 12, 15, 20]
# result = reduce(lambda x, y: x + [y], filter(lambda x: x % 3 != 0, numbers), [])

# print(result)

# Filter out negative numbers from a list(task 11)

# from functools import reduce 

# numbers = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

# my_list = reduce(lambda x,y: x + [y],filter(lambda x: x <0, numbers),[] )

# print(my_list)

#Find the product of all numbers in a list

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# def non_zero(x):
#     return x != 0

# def multiply(x, y):
#     return x * y

# product = reduce(multiply, filter(non_zero, numbers))

# print("Product of all non-zero numbers:", product)

# Concatenate a list of strings

from functools import reduce

strings = ["Hello", " ", "world", "!", " ", "This", " ", "is", " ", "Python"]

def non_empty(string):
    return string.strip() != ""

def map_non_empty(string):
    return string.strip()

def concatenate_strings(str1, str2):
    return str1 + str2

result = reduce(concatenate_strings, map(map_non_empty, filter(non_empty, strings)))

print("Concatenated string:", result)
