import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
x = 0
y = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Copy Mario')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    
    pygame.display.update()



