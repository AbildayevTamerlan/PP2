import pygame, sys
from pygame.locals import *
from functions import *

pygame.init()

# displays
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

# position of mouse
x1, y1 = pygame.mouse.get_pos()
x2, y2 = pygame.mouse.get_pos()

# modes with corresponding functions
modes = {
   "pen": lambda: pygame.draw.line(DISPLAYSURF, curr_color, (x1, y1), (x2, y2), THICKNESS),
   "rect": lambda: pygame.draw.rect(DISPLAYSURF, curr_color, calculate_rect(x1, y1, x2, y2), THICKNESS),
   "circle": lambda: pygame.draw.circle(DISPLAYSURF, curr_color, (x1, y1), calculate_R(x1, y1, x2, y2), THICKNESS),
   "square": lambda: pygame.draw.rect(DISPLAYSURF, curr_color, calculate_square(x1, y1, x2, y2), THICKNESS),
   "right triangle": lambda: pygame.draw.polygon(DISPLAYSURF, curr_color, calculate_right_triangle(x1, y1, x2, y2), THICKNESS),
   "equilateral triangle": lambda: pygame.draw.polygon(DISPLAYSURF, curr_color, calculate_equilateral(x1, y1, x2, y2), THICKNESS),
   "rhombus": lambda: pygame.draw.polygon(DISPLAYSURF, curr_color, calculate_rhombus(x1, y1, x2, y2), THICKNESS),
   "eraser": lambda: pygame.draw.line(DISPLAYSURF, BLACK, (x1, y1), (x2, y2), THICKNESS)
}
mode = "pen"


curr_color = RED

while True:
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

      if event.type == MOUSEBUTTONDOWN and event.button == 1:
         print("LMB pressed!")
         LMBpressed = True

         # sets the initial position for all shapes except pen and eraser
         if mode != "pen" and mode != "eraser":
            x1 = event.pos[0]
            y1 = event.pos[1]

      if event.type == MOUSEMOTION:
         print("Position of the mouse:", event.pos)

         # sets first position for pen and eraser
         if mode == "pen" or mode == "eraser":
            x1 = x2
            y1 = y2

         # second position changes based on mouse motion
         x2 = event.pos[0]
         y2 = event.pos[1]

      if event.type == MOUSEBUTTONUP and event.button == 1:
         print("LMB released!")
         LMBpressed = False

         # draws the final shape onto the base layer
         if mode != "pen" and mode != "eraser":
            if mode in modes:
               modes[mode]()
               base_layer.blit(DISPLAYSURF, (0, 0))

      # changes mode based on input
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
         elif event.key == K_5:
            base_layer.blit(DISPLAYSURF, (0, 0))
            mode = "square"
         elif event.key == K_6:
            base_layer.blit(DISPLAYSURF, (0, 0))
            mode = "right triangle"
         elif event.key == K_7:
            base_layer.blit(DISPLAYSURF, (0, 0))
            mode = "equilateral triangle"
         elif event.key == K_8:
            base_layer.blit(DISPLAYSURF, (0, 0))
            mode = "rhombus"

         # changes the thickness based on input
         if event.key == K_EQUALS and THICKNESS < 25:
            print("increased thickness")
            THICKNESS += 1
         if event.key == K_MINUS and THICKNESS > 1:
            print("reduced thickness")
            THICKNESS -= 1

         if mode != "eraser":
            # changes the color based on input
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

      # updates the display with the base layer when not in pen or eraser mode
      if mode != "pen" and mode != "eraser":
         DISPLAYSURF.blit(base_layer, (0, 0))

      # calls the appropriate draw function
      # also draws temporary figures to control shape
      if LMBpressed:
         if mode in modes:
            modes[mode]()

   pygame.display.update()