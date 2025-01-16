x = 4       # x is of type int
x = "Sally" # x is now of type str


a = 4
A = "Sally"
#A will not overwrite a


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


x, y, z = "Orange", "Banana", "Cherry"


x = y = z = "Orange"


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits


x = 5
y = 10
print(x + y)


x = 5
y = "John"
print(x, y)


#-------------------------
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#-------------------------
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)