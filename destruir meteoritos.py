import pygame, random

pantallaAlto = 680
pantallaAncho = 720
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
        if self.rect.y > pantallaAlto: #reinicia la caida de los meteoros cambiando la posicion del eje x 
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

#crea la clase juego
class juego (object):
    def __init__ (self, sonidoLaser, imagenDeFondo):
        self.puntaje = 0
        self.meteoroLista = pygame.sprite.Group()
        self.totalListaImagenes = pygame.sprite.Group()
        self.cantidadMeteoros = 50
        self.lasersLista = pygame.sprite.Group()
        
        
        for i in range (self.cantidadMeteoros): #crea los meteoros y genera la posicion donde van a comienzar
            meteoros = meteoro()
            meteoros.rect.x = random.randrange(pantallaAncho)
            meteoros.rect.y = random.randrange(pantallaAlto)
            self.meteoroLista.add(meteoros)
            self.totalListaImagenes.add(meteoros)
            
        self.jugador = player()
        self.totalListaImagenes.add(self.jugador)
        self.fondo = pygame.image.load(imagenDeFondo).convert()
        self.sonido = sonidoLaser
        
    def process_events (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                disparo = laser()
                disparo.rect.x = self.jugador.rect.x + 45
                disparo.rect.y = self.jugador.rect.y - 20
           
            
                self.totalListaImagenes.add(disparo)
                self.lasersLista.add(disparo)
                self.sonido.play()
        return False

    def run_logic (self):
        self.totalListaImagenes.update()
        for disparo in self.lasersLista:
            meteoroHitLista = pygame.sprite.spritecollide(disparo, self.meteoroLista, True)
            for meteoro in meteoroHitLista:
                self.totalListaImagenes.remove(disparo)
                self.lasersLista.remove(disparo)
                self.puntaje += 1
                print (self.puntaje)
            if disparo.rect.y < -10 :
                self.totalListaImagenes.remove(disparo)
                self.lasersLista.remove(disparo)
    
    def display_frame (self,ventana):
        ventana.blit(self.fondo,[0,0])
        self.totalListaImagenes.draw(ventana)
        pygame.display.flip()

def main ():
    pygame.init() 
    imagenDeFondo = "recursos/imagenes/background.png"
    sonidoLaser = pygame.mixer.Sound("recursos/sonido/laser5.ogg")
    ventana = pygame.display.set_mode([pantallaAncho, pantallaAlto])
    cerrar = False
    reloj = pygame.time.Clock()
    game = juego( sonidoLaser, imagenDeFondo)
    pygame.mouse.set_visible(0)
   
    while not cerrar:
        cerrar = game.process_events()
        game.run_logic()
        game.display_frame(ventana)
        reloj.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()      

