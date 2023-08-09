import pygame, random
from destruirMeteoritos import pantallaAlto, pantallaAncho
negro = (0,0,0)
class meteoro (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("recursos/imagenes/meteor.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def update (self):
        #genera el moviemiento de caida de los meteoros
        self.rect.y += 1
        if self.rect.y > pantallaAlto: #reinicia la caida de los meteoros cambiando la posicion del eje x 
            self.rect.y = -10
            self.rect.x = random.randrange(pantallaAncho)