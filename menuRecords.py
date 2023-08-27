import pygame
import sys
from registroPuntajes import *

negro = (0,0,0)
blanco = (255, 255,255)
rojo = (255, 0, 0)

def menuRecords(ventana):
    #pygame.init()
    fondo =pygame.image.load("recursos/imagenes/background.png").convert()
    ventana.blit(fondo,[0,0])
    fuenteNombre = pygame.font.Font(None, 45)
    fuentePuntaje = pygame.font.Font(None, 35)
    fuentePuesto = pygame.font.Font(None,50)
    
    #carga los puntajes
    records = listaPuntaje()
    records.leerPuntajes()
    
    #muestra por pantalla los records
    y = 100 #posicion vertical inicial
    actual = records.cabeza
    puesto = 1
    while actual:
        textoNombre = fuenteNombre.render(actual.nombre, True, blanco)
        textoPuntaje = fuentePuntaje.render(str(actual.puntaje), True, rojo)
        textoPuesto = fuentePuesto.render(str(puesto), True, rojo)
        ventana.blit(textoPuesto, (80,y))
        ventana.blit(textoNombre, (100, y))
        ventana.blit(textoPuntaje, (300, y))
        y += 50 #mueve el eje y para el siguiente puntaje
        puesto += 1
        actual = actual.siguiente
    
    #crea boton jugar
    botonJugar = pygame.Rect(600, 500, 100, 50)
    pygame.draw.rect(ventana, rojo, botonJugar, 2)
    textJugar = fuenteNombre.render("Jugar", True, blanco)
    ventana.blit(textJugar, (610,515))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botonJugar.collidepoint(pygame.mouse.get_pos()):
                    return "jugar"
    