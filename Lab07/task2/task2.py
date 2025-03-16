import pygame
import os

pygame.init()
pygame.mixer.init()


WIDTH = 500
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MP3 Player")

# music
playlist = ["track1.mp3", "track2.mp3", "track3.mp3"]
current_track = 0

def play_music():
   pygame.mixer.music.load(playlist[current_track])
   pygame.mixer.music.play()

running = True
play_music()

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
        
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            if pygame.mixer.music.get_busy():
               pygame.mixer.music.pause()
            else:
               pygame.mixer.music.unpause()
            
         if event.key == pygame.K_s:
            pygame.mixer.music.stop()
            
         if event.key == pygame.K_RIGHT:
            current_track = (current_track + 1) % len(playlist)
            play_music()
            
         if event.key == pygame.K_LEFT:
            current_track = (current_track - 1) % len(playlist)
            play_music()

   screen.fill((30, 30, 30))
   pygame.display.flip()

pygame.quit()