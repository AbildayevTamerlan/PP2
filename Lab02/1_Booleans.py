# Example №1
print(10 > 9)
print(10 == 9)
print(10 < 9)


# Example №2
a = 200
b = 33

if b > a:
   print("b is greater than a")
else:
   print("b is not greater than a")


# Example №3
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


# Example №4
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# Example №5
class myclass():
   def __len__(self):
      return 0

myobj = myclass()
print(bool(myobj))


# Example №6
def myFunction() :
   return True

if myFunction():
   print("YES!")
else:
   print("NO!")


# Example №7
x = 200
print(isinstance(x, int))