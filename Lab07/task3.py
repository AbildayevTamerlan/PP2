import pygame

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

   keys = pygame.key.get_pressed()

   if keys[pygame.K_UP] and circle_y > 25:
      circle_y -= 20
   if keys[pygame.K_DOWN] and circle_y < HEIGHT - 25:
      circle_y += 20
   if keys[pygame.K_LEFT] and circle_x > 25:
      circle_x -= 20
   if keys[pygame.K_RIGHT] and circle_x < WIDTH - 25:
      circle_x += 20

   screen.fill((255, 255, 255))
   pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), 25)

   pygame.display.flip()
   clock.tick(60)

pygame.quit()