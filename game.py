import pygame
# tamanho da tela;
width = 1200
height = 600

class player():
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('')

pygame.init()
game_window = pygame.display.set_mode([width, height])
pygame.display.set_caption('jogo 01')

gameloop = True
def draw():
    game_window.fill([255, 255, 0])

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    draw()
    pygame.display.update()
