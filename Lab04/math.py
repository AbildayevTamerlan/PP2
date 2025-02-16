# Task 1
import math

def degrees_to_radians(degrees):
   return degrees * (math.pi / 180)

print(degrees_to_radians(15))

print("-----------------")

# Task 2
def trapezoid_area(a, b, h):
   return ((a + b) * h) / 2

print(trapezoid_area(5, 6, 5))

print("-----------------")

# Task 3
def polygon_area(n, s):
   return (n * s ** 2) / (4 * math.tan(math.pi / n))

print(math.floor(polygon_area(4, 25)))

print("-----------------")

# Task 4
def parallelogram_area(base, height):
   return base * height

print(parallelogram_area(5, 6))