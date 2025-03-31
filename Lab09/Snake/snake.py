import pygame
import random
import time
import sys
from colors import *

pygame.init()

# display
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((HEIGHT, WIDTH))

CELL = 30

# level display
current_level = 1

levelFont = pygame.font.SysFont("Verdana", 32)
levelSurface = levelFont.render(str(current_level), True, BLACK)
levelRect = levelSurface.get_rect()
levelRect.topright = (WIDTH - 4, 0)

# next level frame
frameFont = pygame.font.SysFont("Verdana", 60)
frameSurface = frameFont.render("Next Level", True, WHITE)
frameRect = frameSurface.get_rect()
frameRect.center = (WIDTH // 2, HEIGHT // 2)

# congratulate user with victory
congratsFont = pygame.font.SysFont("Verdana", 60)
congratSurface = congratsFont.render("Congratulations!", True, WHITE)
congratRect = congratSurface.get_rect()
congratRect.center = (WIDTH // 2, HEIGHT // 2)

# draws cells 30x30
def draw_grid():
   for i in range(HEIGHT // CELL):
      for j in range(WIDTH // CELL):
         pygame.draw.rect(screen, GRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# paints the cells with colors
def draw_grid_chess():
   colors = [WHITE, GRAY]

   for i in range(HEIGHT // CELL):
      for j in range(WIDTH // CELL):
         pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# classes
class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def __str__(self):
      return f"{self.x}, {self.y}"

class Snake:
   def __init__(self):
      self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
      self.dx = 1
      self.dy = 0

   def move(self):
      # moves the body of snake by replacing i with i - 1
      for i in range(len(self.body) - 1, 0, -1):
         self.body[i].x = self.body[i - 1].x
         self.body[i].y = self.body[i - 1].y

      self.body[0].x += self.dx
      self.body[0].y += self.dy

      # checks the left border
      if self.body[0].x > WIDTH // CELL - 1:
         self.body[0].x = 0
      # checks the right border
      elif self.body[0].x < 0:
         self.body[0].x = WIDTH // CELL - 1
      # checks the bottom border
      elif self.body[0].y > HEIGHT // CELL - 1:
         self.body[0].y = 0
      # # checks the top border
      elif self.body[0].y < 0:
         self.body[0].y = HEIGHT // CELL - 1

   def draw(self):
      head = self.body[0]
      pygame.draw.rect(screen, RED, (head.x * CELL, head.y * CELL, CELL, CELL))
      for segment in self.body[1:]:
         pygame.draw.rect(screen, YELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

   def check_collision(self, food):
      head = self.body[0]
      if head.x == food.pos.x and head.y == food.pos.y:
         print("Got food!")

         weight = random.randint(1, 3)

         food.count += weight
         if food.count >= 10: # if user ate 5 food, he can ascend to another level
            global current_level, FPS, levelSurface
            if current_level == 3: # if 3 levels are passed, congratulate user
               screen.fill(BLACK)
               screen.blit(congratSurface, congratRect)
               pygame.display.update()
               time.sleep(3)
               pygame.quit()
               sys.exit()

            # changing variables according to the next levels
            current_level += 1
            levelSurface = levelFont.render(str(current_level), True, BLACK)
            FPS += 5
            food.count = 0

            screen.fill(BLACK)
            screen.blit(frameSurface, frameRect)
            pygame.display.update()
            time.sleep(3)

            self.body = [self.body[0], self.body[1], self.body[2]]
         else:
            while weight != 0:
               self.body.append(Point(head.x, head.y))
               weight -= 1

         food.generate_random_pos()

class Food:
   def __init__(self):
      self.pos = Point(9, 9)
      self.count = 0
      self.spawn_time = time.time() # controls spawn time

   def draw(self):
      pygame.draw.rect(screen, GREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

   def generate_random_pos(self):
      while True:
         self.pos.x = random.randint(0, WIDTH // CELL - 1)
         self.pos.y = random.randint(0, HEIGHT // CELL - 1)

         # makes sure food doesn't appear on snake
         if all(segment.x != self.pos.x or segment.y != self.pos.y for segment in snake.body):
            break

      # updates spawn time after spawning
      self.spawn_time = time.time()

# clock         
FPS = 5
clock = pygame.time.Clock()

# objects
food = Food()
snake = Snake()

# main loop
running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

      # сhanges the direction of the snake based on user input
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RIGHT:
            snake.dx = 1
            snake.dy = 0
         elif event.key == pygame.K_LEFT:
            snake.dx = -1
            snake.dy = 0
         elif event.key == pygame.K_DOWN:
            snake.dx = 0
            snake.dy = 1
         elif event.key == pygame.K_UP:
            snake.dx = 0
            snake.dy = -1 

   screen.fill(BLACK)

   draw_grid_chess()

   # displays current level
   screen.blit(levelSurface, levelRect)

   # moves snake and checks collision
   snake.move()
   snake.check_collision(food)

   snake.draw()
   food.draw()

   # if food was spawned 7 seconds ago, it will be respawned
   if time.time() - food.spawn_time > 7:
      food.generate_random_pos()

   pygame.display.flip()
   clock.tick(FPS)

pygame.quit()