import pygame
from time import sleep

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode(0,0) ,pygame.FULLSCREEN

pygame.mixer.music.load("")
pygame.mixer.music.play("")
sleep(5)

pygame.mixer.music.load("")
pygame.mixer.music.play("")
sleep(1)

image = pygame.image.load()
window.blit(image ,(0,0))

pygame.display.update()

sleep(5)
