# 1
class StringOperations:
   def getString(self):
      self.string = input("Enter a string: ")

   def printString(self):
      print(self.string.upper())

string = StringOperations()
string.getString()
string.printString()

print()


# 2
class Shape:
   def area(self):
      print(0)

class Square(Shape):
   def __init__(self, length):
      self.length = length

   def area(self):
      print(self.length * self.length)

s1 = Shape()
s1.area()

s2 = Square(10)
s2.area()

print()


# 3
class Rectangle(Shape):
   def __init__(self, length, width):
      self.length = length
      self.width = width

   def area(self):
      print(self.length * self.width)

s3 = Rectangle(12, 5)
s3.area()

print()


# 4
class Point:
   def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y

   def show(self):
      print(f"({self.x}, {self.y})")

   def move(self, x, y):
      self.x = x
      self.y = y

   def dist(self, point):
      return (((point.x - self.x) ** 2) + ((point.y - self.y) ** 2)) ** 0.5

p1 = Point(1, 5)
p1.show()

p1.move(2, 4)
p1.show()

p2 = Point(1, 5)
print(p1.dist(p2))

print()

# 5
class Account:
   def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance

   def deposit(self, amount):
      self.balance += amount

   def withdraw(self, amount):
      if amount > self.balance:
         print("Insufficient funds on balance.")
      else:
         self.balance -= amount

account = Account("Tamerlan", 47135)
print("Balance: ", account.balance)

account.deposit(47135)
print("Balance: ", account.balance)

account.withdraw(14270)
print("Balance: ", account.balance)

account.withdraw(100000)
print("Balance: ", account.balance)

print()


# 6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 29]
prime_numbers = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int((x ** 0.5)) + 1)), numbers))

print(prime_numbers)