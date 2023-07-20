import pygame, random


ventana = pygame.display.set_mode([720,680])
reloj = pygame.time.Clock()
imagenDeFondo = pygame.image.load("recursos/imagenes/background.png").convert()
cerrar = False
#agrega imagenes para el juego
class meteoro (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.imagen = pygame.image.load("recursos/imagenes/meteor.png").convert()
        self.imagen.set_colorkey([0,0,0,0])
        self.rect = self.imagen.get_rect()
pygame.init()
        
jugador = pygame.image.load("recursos/imagenes/player.png").convert()
jugador.set_colorkey([0,0,0,0])
pygame.mouse.set_visible(0)
meteoroLista = pygame.sprite.Group()
totalListaMeteoros = pygame.sprite.Group()

for i in range (50):
    meteoros = meteoro()
    meteoros.rect.x = random.randrange(720)
    meteoros.rect.y = random.randrange(680)
    meteoroLista.add(meteoros)
    totalListaMeteoros.add(meteoros)
    

while not cerrar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cerrar = True
    
    direcionMouse = pygame.mouse.get_pos()
    #print (direcionMouse)
    x = direcionMouse [0]
    y = direcionMouse [1]
    
    #ventana.fill([255,255,255])
    totalListaMeteoros.draw(ventana)
    ventana.blit(imagenDeFondo,[0,0])
    ventana.blit(jugador, [x,y])
    
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()