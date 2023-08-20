import pygame
import sys

negro = (0,0,0)
blanco = (255, 255,255)
rojo = (255, 0, 0)

def menuJuego (ventana):
    fondo = pygame.image.load("recursos/imagenes/background.png").convert()
    ventana.blit(fondo,(0,0))
    fuente = pygame.font.Font(None, 30)
    
    textJugar = fuente.render("Jugar", True, blanco)
    textRecords = fuente.render("Ver Records", True, blanco)
    
    opcionJugar = pygame.Rect(300, 200, 100, 50)
    opcionVerRecords = pygame.Rect(300, 300, 100, 50)
    
    pygame.draw.rect(ventana, rojo, opcionJugar, 2)
    pygame.draw.rect(ventana, rojo, opcionVerRecords, 2)
    
    ventana.blit(textJugar, (315, 215))
    ventana.blit(textRecords, (315, 315))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if opcionJugar.collidepoint(pygame.mouse.get_pos()):
                    return "jugar"
                if opcionVerRecords.collidepoint(pygame.mouse.get_pos()):
                    return "records"
    
    