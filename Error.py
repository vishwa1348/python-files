# Write a Python program that asks the user to input a number and prints the reciprocal of that number. Handle the exception if the user inputs zero (task :1)

# try :
#     num = float(input("Enter a number :")) 
#     print(1/num)
# except :
#     print("error")

# Modify the above program to also handle the exception if the user inputs a non-numeric value(task :2)

# try:
#     num = int(input("Enter the numerator: "))
#     sum = int(input("Enter the denominator: "))
#     result = num / sum
#     print(f"{result}")
    
# except Exception as e:
#     print("Error",e)
    
# Write a program that reads a number from the user and prints its square. Use the else clause to print a success message(task :3)

# power = input("Enter a number :")
# try:
#     number = int(power)

# except ValueError:
#     print("error")

# else:
#     square = number**2
#     print("result :",square)
#     print("success")

# Modify the program in Task 3 to include a finally clause that prints a message regardless of whether an exception occurred or not(task :4)

# try:
#     power = input("Enter a number :")
#     number = int(power)
#     square = number**2
#     print("result :",square)

# except ValueError:
#     print("error")

# finally:
#     print("program completed")


# Write a function that raises a ValueError if the input number is negative(task :5)

# try:
#     result = int(input("Enter a number :"))
#     print("Input number is:", result) 

# except ValueError as e:
#     print(e)

# Write a program that repeatedly asks the user for a number and handles exceptions. The program should continue asking until a valid number is entered(task :6)

# try:
#     user = input("Enter a number :")
#     number = float(user)
#     print(f"answer",number)

# except ValueError:
#     print("Invailed number")
