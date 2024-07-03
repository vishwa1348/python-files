#  Generate a random float between 0 and 1(task :1)

# type: ignore ##import random 
##
##print(random.random())

## Generate a random integer between two numbers

##import random
##
##print(random.randrange(1,10))

##Choose a random element from a list

##import random
##a = ["air","water","land"]
##
##print(random.choice(a))

## Shuffle a list in place

##import random
##
##a = ["air","water","land"]
##
##random.shuffle(a)
##print (a)

##Generate a random sample of elements from a list

##import random
##
##mylist = ["apple", "banana", "cherry"]
##
##print(random.sample(mylist, k=2))

##Generate a random even number between 0 and 100.

##import random
##
##for x in range(6):
##    print(random.randrange(10,100,2))

##Generate a random odd number between 1 and 99.

##import random
##
##for x in range(7):
##    print(random.randrange(11,99,3))

##=======================================================

##Generate a random password of length 8 containing letters and digits

##import random
##import string
##
##n = 32
##
##res = ''.join(random.choice(string.ascii_uppercase + string_digits))
##for i in range(n):
##    print("generated password :" ,''+ str(res))

##import random
##import string
##
##def generate_random_string(length):
##
##	letters = string.ascii_letters
##	random_string = ''.join(random.choice(letters) for i in range(length))
##	return random_string
##
##random_string = generate_random_string(8)
##print(random_string)

##Generate a random date within the current year

# from datetime import date
# import random

# start_dt = date.today().replace(day=1, month=1).toordinal()
# end_dt = date.today().toordinal()
# random_day = date.fromordinal(random.randint(start_dt, end_dt))
# print(random_day)

# import random  # type: ignore

# vs = ["apple","banana","kiwi","mango","iceapple"]

# items = random.choices(vs)

# while True :
#     answer = input("guess an item from this list (apple,banana,kiwi,mango,iceapple):").lower()
#     if answer== items:
#         print("It is the right answer!")
#     else:
#         again = input("ur is guess is wrong. Do u want to try again say (yes \ no)").lower()
#         if again != 'yes':
#             break
#         else:
#             continue








