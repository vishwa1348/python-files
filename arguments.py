#sum of all arguments 

# def numbers(*num):
#     sum = 0
#     for i in num:
#         sum = sum + i 
#     print("total is ",sum)
# numbers(1,2,3,4,5)

#Multiply all arguments

# def numbers(*num):
#     multiple = 1
#     for i in num:
#         multiple = multiple *i
#     print("total is", multiple)

# numbers(1,2,3,4,5)

#Concatenate all arguments

# def numbers(*num):
#     sum = ' '.join(num)
#     return sum
# result = numbers ("hello","world","!")
# print(result)

#Print arguments and keywords
#arguments

# def name(*kid):
#     sum = "He is my elder son " + kid[0]
#     print(sum)

# name("adhvai","ishwariya")

#keywords

# def name(**key):
#     for i in key:
#         print(key)
# name(Name ="adhvai", age = "13")

# Add Two Numbers

# desk = lambda a,b: print(a+b)
# desk(13,8)

# Find the Maximum of Two Numbers

# top = lambda a,b : a if (a>b) else b
# print(top(234,324))

# Square a Number

# line = lambda a: a**2
# result = line(3243543478897906785)
# print(result)

# Reverse a String

# space = lambda s: s[::-1]
# nothing = "hello"
# space = space(nothing)
# print(space)

# Check if a Number is Even


# even = lambda x: x % 2 == 0
# num = 10
# if even(num):
#     print(num, "is even")

