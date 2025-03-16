import pygame
import datetime

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# images
clock_image = pygame.image.load("clock.png")
min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")

# center of the clock
center_x, center_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

   # current time
   now = datetime.datetime.now()
   minutes = now.minute
   seconds = now.second

   # angle of the clock hands
   angle_min = -(minutes * 6)
   angle_sec = -(seconds * 6)

   # rotate the clock hands
   rotated_min_hand = pygame.transform.rotate(min_hand, angle_min)
   rotated_sec_hand = pygame.transform.rotate(sec_hand, angle_sec)

   min_rect = rotated_min_hand.get_rect(center = (center_x, center_y))
   sec_rect = rotated_sec_hand.get_rect(center = (center_x, center_y))
  
   screen.fill((255, 255, 255))
   screen.blit(clock_image, (0, 0))
   screen.blit(rotated_min_hand, min_rect.topleft)
   screen.blit(rotated_sec_hand, sec_rect.topleft)

   pygame.display.flip()
   clock.tick(30)

pygame.quit()