# Task 1
def square_gen(stop):
   start = 0
   while start <= stop:
      yield start ** 2
      start += 1

for square in square_gen(25):
   print(square)

print("-----------------")

# Task 2
def even_num_gen(stop):
   if stop % 2 != 0:
      stop -= 1

   start = 0
   while start < stop:
      yield f"{start}, "
      start += 2
   yield stop

for even_num in even_num_gen(101):
   print(even_num, end = "")

print("\n-----------------")

# Task 3
def div_by_12_gen(stop):
   start = 0
   while start <= stop:
         yield start
         start += 12

for num in div_by_12_gen(1000):
   print(num, end = " ")

print("\n-----------------")

# Task 4
def squares(a, b):
   while a <= b:
      yield a ** 2
      a += 1

for square in squares(5, 13):
   print(square)

print("-----------------")

# Task 5
def printing(num):
   while num >= 0:
      yield num
      num -= 1

for num in printing(100):
   print(num, end = " ")