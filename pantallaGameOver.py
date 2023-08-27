import pygame, sys
from constantes import *
ventana = pygame.display.set_mode([pantallaAncho, pantallaAlto])
puntaje = 100

def mostrarGameOver (ventana, puntaje):
    pygame.init()
    fondo = pygame.image.load("recursos/imagenes/background.png").convert()
    ventana.blit(fondo,[0,0])
    fuenteGameOver = pygame.font.SysFont("serif", 40)
    texto = fuenteGameOver.render("o pulse [Esc] para salir al menu", True, rojo)
    texto2 = fuenteGameOver.render("Muerto. Pulsar [barra] para volver a empezar", True, rojo)
    centroX = (pantallaAncho // 2) - (texto.get_width() // 2)
    centroY = (pantallaAlto // 2) - (texto.get_height() // 2)
    centroXTex2 = (pantallaAncho // 2) - (texto2.get_width() // 2)
    centroYTex2 = (pantallaAlto // 3) - (texto2.get_height() // 3)
    ventana.blit(texto,[centroX,centroY])
    ventana.blit(texto2,[centroXTex2,centroYTex2])
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
mostrarGameOver(ventana, puntaje)