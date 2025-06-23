def victory():
    import pygame, sys
    from controles import controles
    pygame.init()
    pygame.mixer.init()
    size = (360,640)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

        #-------IMAGENES-------
        #Cargar imagenes
    fondo = pygame.image.load("Assets/Espacio/bg1.png")
    cosmos = pygame.image.load("Assets/Espacio/bg4.png")
    victory = pygame.image.load("Assets/Victory/you_win.png")
    retry_apagado = pygame.image.load("Assets/Victory/retry_apagado.png")
    retry_brillo = pygame.image.load("Assets/Victory/retry_brillo.png")
    quit_apagado = pygame.image.load("Assets/Victory/quit_apagado.png")
    quit_brillo = pygame.image.load("Assets/Victory/quit_brillo.png")

        #Escalar imagenes
    victory = pygame.transform.scale(victory,(250,150))
    retry_apagado = pygame.transform.scale(retry_apagado,(150,40))
    retry_brillo = pygame.transform.scale(retry_brillo,(150,40))
    quit_apagado = pygame.transform.scale(quit_apagado,(120,40))
    quit_brillo = pygame.transform.scale(quit_brillo,(120,40))

        #posición imagenes
    victory_rect =victory.get_rect(center=(size[0]//2,200))
    retry_rect = retry_apagado.get_rect(center=(size[0]//2,350))
    quit_rect = quit_apagado.get_rect(center=(size[0]//2,450))

        #Velocidad fondo
    cosmos_y = 0
    velocidad_cosmos = 2
    fondo_y = 0
    velocidad_fondo = 1

        #Game Over parpadeante
    mostrar_victory = True
    tiempo_parpadeo = 350
    ultimo_cambio = pygame.time.get_ticks()


        #-------SONIDO-------   
        #Sonidos
    boton = pygame.mixer.Sound("Assets/Sonidos/boton2.wav")
    boton.set_volume(0.5)

        #(Para el sonido de los botones)
    retry_hovered_old = False
    quit_hovered_old = False

        #-------BUCLE-------
    while True:
            #Ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            
                #Colisiones para botones
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    return "retry"
                elif quit_rect.collidepoint(event.pos):
                    return "quit"
                    #----------
            
            #Mouse
        mouse_pos = pygame.mouse.get_pos()
        retry_hovered = retry_rect.collidepoint(mouse_pos)
        quit_hovered = quit_rect.collidepoint(mouse_pos)
                
            #-------FONDO-------
        fondo_y += velocidad_fondo
        cosmos_y += velocidad_cosmos
        if cosmos_y >=640:
            cosmos_y = 0
        if fondo_y >=640:
                fondo_y = 0

            #Fondo
        screen.blit(fondo, (0,fondo_y))
        screen.blit(fondo, (0, fondo_y - 640))
        screen.blit(cosmos, (0,cosmos_y))
        screen.blit(cosmos, (0, cosmos_y - 640))
            
            #Game over
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultimo_cambio >= tiempo_parpadeo:
            mostrar_victory = not mostrar_victory
            ultimo_cambio = tiempo_actual
            
        if mostrar_victory:
            screen.blit(victory, victory_rect.topleft)
            
            #Botones
        if retry_hovered:
            screen.blit(retry_brillo, retry_rect.topleft)
        else:
            screen.blit(retry_apagado, retry_rect.topleft)
                
        if quit_hovered:
            screen.blit(quit_brillo, quit_rect.topleft)
        else:
            screen.blit(quit_apagado, quit_rect.topleft)
                
                #----------
                
            #-------SONIDO-------
            #Sonido botones
        if retry_hovered and not retry_hovered_old:
            boton.play()
        if quit_hovered and not quit_hovered_old:
            boton.play()

            
            #Actualizo los sonidos
        retry_hovered_old = retry_hovered
        quit_hovered_old = quit_hovered

            #Actualizo la pantalla
        pygame.display.flip()
        clock.tick(60)