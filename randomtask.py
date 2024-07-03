##random task

import random  # type: ignore

vs = ["apple","banana","kiwi","mango","iceapple"]

while True :
    items = random.choices(vs)
    answer = input("guess an item from this list (apple,banana,kiwi,mango,iceapple):").lower()
    if answer== items:
        print("It is the right answer!")
    else:
        print("your guess is wrong ")

    again = input(" Do u want to try again say (yes \ no)").lower()
    if again != 'yes':
        break
    else:
        continue



