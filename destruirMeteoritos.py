import pygame, random, time, sys
from jugadorYLaser import *
from METEORO import *

pantallaAlto = 680
pantallaAncho = 720
negro = (0,0,0)
blanco = (255, 255,255)
rojo = (255, 0, 0)

#crea la clase juego
class juego (object):
    def __init__ (self, sonidoLaser, imagenDeFondo):
        self.gameOver = False
        self.puntaje = 0
        self.meteoroLista = pygame.sprite.Group()
        self.totalListaImagenes = pygame.sprite.Group()
        self.cantidadMeteoros = 5
        self.lasersLista = pygame.sprite.Group()
        self.meteorosAgregadosXNivel = 5
        self.velocidadMeteoros = 0
            
        self.jugador = player()
        self.vidasJugador = 4
        self.jugador.rect.x = (pantallaAncho - self.jugador.rect.width )// 2
        self.jugador.rect.y = pantallaAlto - self.jugador.rect.height
        self.totalListaImagenes.add(self.jugador)
        self.fondo = pygame.image.load(imagenDeFondo).convert()
        self.sonido = sonidoLaser
        
        self.entreTiempo = 3
        self.ultimaTanda = time.time()
        self.reiniciarJuego()
    
    def reiniciarJuego (self):
        self.gameOver = False
        self.puntaje = 0
        self.velocidadMeteoros = 0
        self.meteoroLista.empty()
        self.totalListaImagenes.empty()
        self.lasersLista.empty()
        self.cantidadMeteoros = 5
        self.entreTiempo = 3
        self.ultimaTanda = time.time()
        self.jugador = player()
        self.vidasJugador = 4
        self.totalListaImagenes.add(self.jugador)
        self.jugador.rect.x = (pantallaAncho - self.jugador.rect.width )// 2
        self.jugador.rect.y = pantallaAlto - self.jugador.rect.height
    
    def crearTandasMeteoros(self): 
        self.velocidadMeteoros += 0.1
        for i in range (self.cantidadMeteoros): #crea los meteoros y genera la posicion donde van a comienzar
            meteoros = meteoro()
            meteoros.rect.x = random.randrange(pantallaAncho)
            meteoros.rect.y = random.randrange(250)#pantallaAlto)
            meteoros.velocidadCaida += self.velocidadMeteoros
            self.meteoroLista.add(meteoros)
            self.totalListaImagenes.add(meteoros)
        print("velocidad de caida ", meteoros.velocidadCaida)
            
        
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.gameOver:
                       self.reiniciarJuego()
           
        return False

    def run_logic (self):
        tiempoActual = time.time()
        if not self.gameOver:
            self.totalListaImagenes.update()
            for disparo in self.lasersLista:
                meteoroHitLista = pygame.sprite.spritecollide(disparo, self.meteoroLista, True)
                for meteoro in meteoroHitLista:
                    self.totalListaImagenes.remove(disparo)
                    self.lasersLista.remove(disparo)
                    self.puntaje += 1
                    #print (self.puntaje)
                if disparo.rect.y < -10 :
                    self.totalListaImagenes.remove(disparo)
                    self.lasersLista.remove(disparo)
            if not self.meteoroLista:
                if tiempoActual - self.ultimaTanda >= self.entreTiempo:
                    self.cantidadMeteoros += self.meteorosAgregadosXNivel
                    print ("alerta")
                    self.crearTandasMeteoros()
            if pygame.sprite.spritecollide(self.jugador,self.meteoroLista,True):
                self.vidasJugador -= 1
                if self.vidasJugador == 0:
                    self.gameOver = True
                    #print("muerto")

    
    def display_frame (self,ventana):
        ventana.blit(self.fondo,[0,0])
        #puntaje
        fuente = pygame.font.SysFont("serif", 25)
        textoPuntaje = fuente.render("Puntaje: " + str(self.puntaje), True, blanco)
        esquinaXIzquierda = 10
        esquinaYInfe = pantallaAlto - 40
        ventana.blit(textoPuntaje,[esquinaXIzquierda, esquinaYInfe])
        #barra de vida
        maximoVida = 5
        longitudBarraVida = 200
        longitudBarraVidaActual = longitudBarraVida * self.vidasJugador / maximoVida
        esquinaXDerecha = pantallaAncho - longitudBarraVida - 10
        pygame.draw.rect(ventana, rojo, (esquinaXDerecha, esquinaYInfe, longitudBarraVidaActual, 20))
        
        if self.gameOver:
            fuenteGameOver = pygame.font.SysFont("serif", 40)
            texto = fuenteGameOver.render("Muerto. Pulsar barra para volver a empezar", True, rojo)
            centroX = (pantallaAncho // 2) - (texto.get_width() // 2)
            centroY = (pantallaAlto // 2) - (texto.get_height() // 2)
            ventana.blit(texto,[centroX,centroY])
        if not self.gameOver:
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

