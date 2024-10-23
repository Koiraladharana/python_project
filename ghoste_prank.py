import pygame
from time import sleep

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode(0,0) ,pygame.FULLSCREEN

pygame.mixer.music.load("gu_cheng.mp3")
pygame.mixer.music.play("")
sleep(5)

pygame.mixer.music.load("the_untamed.mp3")
pygame.mixer.music.play("")
sleep(1)

image = pygame.image.load(ghost.pgp)
window.blit(image ,(0,0))

pygame.display.update()

sleep(5)
