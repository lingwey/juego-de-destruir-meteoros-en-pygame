import pygame, random

pantallaAlto = 680
pantallaAncho = 720
ventana = pygame.display.set_mode([pantallaAncho, pantallaAlto])
reloj = pygame.time.Clock()
imagenDeFondo = pygame.image.load("recursos/imagenes/background.png").convert()
cerrar = False
negro = (0,0,0)

#agrega imagenes para el juego
class meteoro (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("recursos/imagenes/meteor.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def update (self):
        #genera el moviemiento de caida de los meteoros
        self.rect.y += 1
        if self.rect.y > pantallaAlto: #reinicia la caida de los meteoros cambiando la posicion del eje 3 
            self.rect.y = -10
            self.rect.x = random.randrange(pantallaAncho)
    
        
class player (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("recursos/imagenes/player.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def update (self): #controla los movimeintos del jugador y mantiene limpio el codiog del bucle principal
        direcionMouse = pygame.mouse.get_pos()
         #print (direcionMouse)
        jugador.rect.x = direcionMouse [0]
        jugador.rect.y = direcionMouse [1]

class laser (pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("recursos/imagenes/laser.png")
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def update (self): 
        self.rect.y -= 5
        
        
pygame.init()       
#jugador = pygame.image.load("recursos/imagenes/player.png").convert()
#jugador.set_colorkey([0,0,0,0])
pygame.mouse.set_visible(0)
meteoroLista = pygame.sprite.Group()
lasersLista = pygame.sprite.Group()
totalListaImagenes = pygame.sprite.Group()
jugador =player()
puntaje = 0
totalListaImagenes.add(jugador)

for i in range (50): #crea los meteoros y genera la posicion donde van a comienzar
    meteoros = meteoro()
    meteoros.rect.x = random.randrange(pantallaAncho)
    meteoros.rect.y = random.randrange(pantallaAlto)
    meteoroLista.add(meteoros)
    totalListaImagenes.add(meteoros)
    
sonidoLaser = pygame.mixer.Sound("recursos/sonido/laser5.ogg")

while not cerrar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cerrar = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            disparo = laser()
            disparo.rect.x = jugador.rect.x + 45
            disparo.rect.y = jugador.rect.y - 20
           
            
            totalListaImagenes.add(disparo)
            lasersLista.add(disparo)
            sonidoLaser.play()
       
    #el metodo update remplaza todo este bloque de codigo     
    """direcionMouse = pygame.mouse.get_pos()
    #print (direcionMouse)
    jugador.rect.x = direcionMouse [0]
    jugador.rect.y = direcionMouse [1] """
    
    totalListaImagenes.update() #genera el movimiento a toda la lista de sprites 
    
    """meteoroHitLista = pygame.sprite.spritecollide(jugador, meteoroLista, True)
    for meteor in meteoroHitLista:
        puntaje += 1
        print(puntaje)"""
    for disparo in lasersLista:
        meteoroHitLista = pygame.sprite.spritecollide(disparo, meteoroLista, True)
        for meteoro in meteoroHitLista:
            totalListaImagenes.remove(disparo)
            lasersLista.remove(disparo)
            puntaje += 1
            print (puntaje)
        if disparo.rect.y < -10 :
            totalListaImagenes.remove(disparo)
            lasersLista.remove(disparo)
    #ventana.fill([255,255,255])
    ventana.blit(imagenDeFondo,[0,0])
    #ventana.blit(jugador, [x,y])
    totalListaImagenes.draw(ventana)
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()