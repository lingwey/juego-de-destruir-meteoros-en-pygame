import pygame
negro = (0,0,0)
class player (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("recursos/imagenes/player.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def update (self): #controla los movimeintos del jugador y mantiene limpio el codiog del bucle principal
        direcionMouse = pygame.mouse.get_pos()
         #print (direcionMouse)
        self.rect.x = direcionMouse [0]
        self.rect.y = direcionMouse [1]

class laser (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("recursos/imagenes/laser.png")
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def update (self): 
        self.rect.y -= 5