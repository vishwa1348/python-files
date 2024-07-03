#string method
#capitalize
a = "hello, and welcome to my world"
print(a.capitalize())

#casefold
a = "hello, and welcome to my world"
print(a.casefold())

#center
a ="hello"
print(a.center(20))

#count
a = "hello, and welcome to my world"
print(a.count("hello")) 

#encode
a = "hello, and welcome to my world"
print(a.encode())

#endswith
a = "hello, and welcome to my world@#$%"
print(a.endswith("%"))

#expandtabs
a = "\th\te\tl\tl\to"
print(a.expandtabs())

#find(index number)
a = "hello, and welcome to my world"
print(a.find("to"))

#isalnum
a = "world3456"
print(a.isalnum())

#isalpha
a = "world"
print(a.isalpha())

#isascii
a = "world3456"
print(a.isascii())

#isdecimal
a = "3456"
print(a.isdecimal())

#isdigit
a = "3456"
print(a.isdigit())

#isidentifier
a = "world"
print(a.isidentifier())

#islower
a = "world3456"
print(a.islower())

#isnumeric
a = "world3456"
print(a.isnumeric())

#isprintable
a =  "world3456"
print(a.isprintable())

#isspace
a = "  "
print(a.isspace())

#istitle
a = "Hello, And Welcome To My World!"
print(a.istitle())

#isupper
a = "HELLO, AND WELCOME TO MY WORLD!"
print(a.isupper())

#join
a = ("Hello","And","Welcome","To","My","World")
print("[]".join(a))

#Ijust
a = "apple"
s = a.ljust(10)
print(s,"is my favorite fruit")

#lower
a = "Hello World"
print(a.lower())

#lstrip
v = "    apple"
s = v.lstrip()
print("Out of all fruits",s,"is my favorite")

#maketrans
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

#partition
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)
