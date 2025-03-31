import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH = 800
HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((WIDTH , HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

# colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

LMBpressed = False
THICKNESS = 5

x1, y1 = pygame.mouse.get_pos()
x2, y2 = pygame.mouse.get_pos()

mode = "pen"

curr_color = RED
last_color = curr_color

def calculate_rect(x1, y1, x2, y2):
   return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1-x2), abs(y1-y2))

def calculate_R(x1, y1, x2, y2):
   a = abs(x2 - x1)
   b = abs(y2 - y1)
   return round((a**2 + b ** 2) ** 0.5)

while True:
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

      if event.type == MOUSEBUTTONDOWN and event.button == 1:
         print("LMB pressed!")
         LMBpressed = True

         if mode == "rect" or mode == "circle":
            x1 = event.pos[0]
            y1 = event.pos[1]

      if event.type == MOUSEMOTION:
         print("Position of the mouse:", event.pos)

         if mode == "pen" or mode == "eraser":
            x1 = x2
            y1 = y2

         x2 = event.pos[0]
         y2 = event.pos[1]

      if event.type == MOUSEBUTTONUP and event.button == 1:
         print("LMB released!")
         LMBpressed = False

         if mode == "rect":
            pygame.draw.rect(DISPLAYSURF, curr_color, calculate_rect(x1, y1, x2, y2), THICKNESS)
            base_layer.blit(DISPLAYSURF, (0, 0))
         elif mode == "circle":
            pygame.draw.circle(DISPLAYSURF, curr_color, (x1, y1), calculate_R(x1, y1, x2, y2), THICKNESS)
            base_layer.blit(DISPLAYSURF, (0, 0))

      if event.type == KEYDOWN:
         if event.key == K_1:
            mode = "pen"
         elif event.key == K_2:
            base_layer.blit(DISPLAYSURF, (0, 0))
            mode = "rect"
         elif event.key == K_3:
            base_layer.blit(DISPLAYSURF, (0, 0))
            mode = "circle"
         elif event.key == K_4:
            mode = "eraser"

         if event.key == K_EQUALS and THICKNESS < 25:
            print("increased thickness")
            THICKNESS += 1
         if event.key == K_MINUS and THICKNESS > 1:
            print("reduced thickness")
            THICKNESS -= 1

         if mode != "eraser":
            if event.key == K_r:
               curr_color = RED
            elif event.key == K_g:
               curr_color = GREEN
            elif event.key == K_b:
               curr_color = BLUE
            elif event.key == K_y:
               curr_color = YELLOW
            elif event.key == K_w:
               curr_color = WHITE

      if mode == "rect" or mode == "circle":
         DISPLAYSURF.blit(base_layer, (0, 0))

      if LMBpressed:
         if mode == "pen":
            pygame.draw.line(DISPLAYSURF, curr_color, (x1, y1), (x2, y2), THICKNESS)
         elif mode == "rect":
            pygame.draw.rect(DISPLAYSURF, curr_color, calculate_rect(x1, y1, x2, y2), THICKNESS)
         elif mode == "circle":
            pygame.draw.circle(DISPLAYSURF, curr_color, (x1, y1), calculate_R(x1, y1, x2, y2), THICKNESS)
         elif mode == "eraser":
            pygame.draw.line(DISPLAYSURF, BLACK, (x1, y1), (x2, y2), THICKNESS)

   pygame.display.update()