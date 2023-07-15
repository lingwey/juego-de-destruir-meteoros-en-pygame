import pygame

ventana = pygame.display.set_mode([720,680])
reloj = pygame.time.Clock()

cerrar = False
#agrega imagenes para el juego
imagenDeFondo = pygame.image.load("recursos/imagenes/background.png").convert()
jugador = pygame.image.load("recursos/imagenes/player.png").convert()
jugador.set_colorkey([0,0,0,0])

while not cerrar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cerrar = True
    
    direcionMouse = pygame.mouse.get_pos()
    #print (direcionMouse)
    x = direcionMouse [0]
    y = direcionMouse [1]
    
    #ventana.fill([255,255,255])
    ventana.blit(imagenDeFondo,[0,0])
    ventana.blit(jugador, [x,y])
    
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()