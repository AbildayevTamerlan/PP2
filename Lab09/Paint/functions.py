import pygame, sys
from pygame.locals import *

def calculate_rect(x1, y1, x2, y2):
   return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_R(x1, y1, x2, y2):
   a = abs(x2 - x1)
   b = abs(y2 - y1)
   return round((a**2 + b**2) ** 0.5)

def calculate_square(x1, y1, x2, y2):
   side = min(abs(x2 - x1), abs(y2 - y1))  # determine the side length
    
   # determine the top-left corner of the square
   if x2 > x1:
      top_left_x = x1
   else:
      top_left_x = x1 - side
   if y2 > y1:
      top_left_y = y1  
   else:
      top_left_y = y1 - side 

   return pygame.Rect(top_left_x, top_left_y, side, side)

def calculate_right_triangle(x1, y1, x2, y2):
   return [(x1, y1), (x2, y1), (x1, y2)]

def calculate_equilateral(x1, y1, x2, y2):
   side = abs(x2 - x1)
   height = round(((3 ** 0.5) / 2) * side)  # calculate height using equilateral triangle formula

   # determine the three points of the triangle
   if y2 < y1:  # triangle points upwards
      top = (x1, y1 - height)
      left = (x1 - side // 2, y1)
      right = (x1 + side // 2, y1)
   else:  # triangle points downwards
      top = (x1, y1 + height)
      left = (x1 - side // 2, y1)
      right = (x1 + side // 2, y1)

   return [top, left, right]

def calculate_rhombus(x1, y1, x2, y2):
   dx, dy = abs(x2 - x1), abs(y2 - y1)  # calculate distances along x and y
   return [(x1, y1 - dy), (x1 + dx, y1), (x1, y1 + dy), (x1 - dx, y1)]  # return rhombus vertices