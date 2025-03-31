import random
import time
import pygame, sys
from pygame.locals import *

pygame.init()

# display
WIDTH = 400
HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# clock
clock = pygame.time.Clock()
FPS = 60

# loading images
image_background = pygame.image.load("resources/AnimatedStreet.png")
image_player = pygame.image.load("resources/Player.png")
image_enemy = pygame.image.load("resources/Enemy.png")
image_coin = pygame.image.load("resources/Coin.png")

# loading sound
pygame.mixer.music.load("resources/background.wav")
pygame.mixer.music.play(-1)

sound_crash = pygame.mixer.Sound("resources/crash.wav")

# text at the end
fontObj = pygame.font.SysFont("Verdana", 60)
surfaceObj = fontObj.render("Game Over", True, "black")
rectObj = surfaceObj.get_rect()
rectObj.center = (WIDTH // 2, HEIGHT // 2)

# coins counter
count = 0

counterFont = pygame.font.SysFont("Verdana", 60)
counterSurface = counterFont.render(str(count), True, "white")
counterRect = counterSurface.get_rect()
counterRect.topright = (WIDTH - 2, 0)

# controls the speed of the enemy based on 'count'
bound = 50

# classes
class Coin(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = image_coin
      self.rect = self.image.get_rect()
      self.rect.bottom = HEIGHT - self.rect.height

   def generate_random_position(self):
      self.rect.left = random.randint(0, WIDTH - self.rect.width)
      self.rect.bottom = random.randint(HEIGHT - (2 * self.rect.height), HEIGHT)

class Enemy(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = image_enemy
      self.rect = self.image.get_rect()
      self.speed = 10

   def generate_random_position(self):
      self.rect.left = random.randint(0, WIDTH - self.rect.width)
      self.rect.bottom = 0

   def move(self):
      self.rect.move_ip(0, self.speed)
      if self.rect.top > HEIGHT:
         self.generate_random_position()

class Player(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = image_player
      self.rect = self.image.get_rect()
      self.rect.midbottom = (WIDTH // 2, HEIGHT)
      self.speed = 5

   def move(self):
      keys = pygame.key.get_pressed()

      if keys[K_RIGHT]:
         if (WIDTH - self.rect.right) > self.speed:
            self.rect.move_ip(self.speed, 0)
         else:
            sound_crash.play()
      elif keys[K_LEFT]:
         if self.rect.left > self.speed:
            self.rect.move_ip(-self.speed, 0)
         else:
            sound_crash.play()

# objects
player = Player()
enemy = Enemy()
coin = Coin()

# sprites
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy)
enemy_sprites.add(enemy)
player_sprites.add(player)

# main loop
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

   DISPLAYSURF.blit(image_background, (0, 0))
   DISPLAYSURF.blit(coin.image, coin.rect)

   counterSurface = counterFont.render(str(count), True, "white")
   DISPLAYSURF.blit(counterSurface, counterRect)

   for entity in all_sprites: # blits and moves player and enemy
      entity.move()
      DISPLAYSURF.blit(entity.image, entity.rect)

   if pygame.sprite.spritecollideany(player, enemy_sprites): # checks collision of player and enemy
      sound_crash.play()
      time.sleep(1)

      # ending frame
      DISPLAYSURF.fill("red")
      DISPLAYSURF.blit(surfaceObj, rectObj)
      pygame.display.update()
      time.sleep(3)

      pygame.quit()
      sys.exit()

   if pygame.sprite.spritecollideany(coin, player_sprites): # collecting coins
      coin.generate_random_position()

      # randomly determines the weight of coins, and adds to the counter
      weight = random.randint(1, 10)
      count += weight

      # increases enemy's speed after each 50 coins
      if count >= bound:
         enemy.speed += 1
         bound += 50
      
      if len(str(count)) > 1: # changes the position of counter if needed
         counterRect.topright = (WIDTH - (len(str(count)) - 1) * counterRect.width, 0)
   
   pygame.display.update()
   clock.tick(FPS)