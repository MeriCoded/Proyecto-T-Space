def menu():
    import pygame, sys
    from controles import controles
    pygame.init()
    pygame.mixer.init()
    size = (360,640)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    #-------IMAGENES-------
    #Cargar imagenes
    background = pygame.image.load("Assets/Espacio/bg1.png")
    cosmos = pygame.image.load("Assets/Espacio/bg4.png")
    logo = pygame.image.load("Assets/Menu/logo.png")
    play_off = pygame.image.load("Assets/Menu/play_off.png")
    play_on = pygame.image.load("Assets/Menu/play_on.png")
    quit_off = pygame.image.load("Assets/Menu/quit_off.png")
    quit_on = pygame.image.load("Assets/Menu/quit_on.png")
    control_off = pygame.image.load("Assets/Menu/control_off.png")
    control_on = pygame.image.load("Assets/Menu/control_on.png")


    #Escalar imagenes
    logo = pygame.transform.scale(logo,(290,110))
    play_off = pygame.transform.scale(play_off,(150,60))
    play_on = pygame.transform.scale(play_on,(150,60))
    quit_off= pygame.transform.scale(quit_off,(150,60))
    quit_on = pygame.transform.scale(quit_on,(150,60))
    control_off = pygame.transform.scale(control_off,(47,34))
    control_on = pygame.transform.scale(control_on,(47,34))

    #posición imagenes
    logo_rect = logo.get_rect(center=(size[0]//2,200))
    play_rect = play_off.get_rect(center=(size[0]//2,350))
    quit_rect = quit_off.get_rect(center=(size[0]//2,450))
    control_rect = control_off.get_rect(center=(size[0]//9,40))

    #Velocidad fondo
    cosmos_y = 0
    velocidad_cosmos = 2
    background_y = 0
    velocidad_background = 1

    #-------SONIDO-------   
    #Sonidos
    pygame.mixer.music.load("Assets/Sonidos/beat.wav")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    boton = pygame.mixer.Sound("Assets/Sonidos/boton2.wav")
    boton.set_volume(0.5)

    #(Para el sonido de los botones)
    play_hovered_old = False
    quit_hovered_old = False
    control_hovered_old = False

    #-------BUCLE-------
    while True:
        #Ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            #Colisiones para botones
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    return
                elif control_rect.collidepoint(event.pos):
                    controles()
                elif quit_rect.collidepoint(event.pos):
                    sys.exit()
                #----------
        
        #Mouse
        mouse_pos = pygame.mouse.get_pos()
        play_hovered = play_rect.collidepoint(mouse_pos)
        quit_hovered = quit_rect.collidepoint(mouse_pos)
        control_hovered = control_rect.collidepoint(mouse_pos)
            
        #-------FONDO-------
        background_y += velocidad_background
        cosmos_y += velocidad_cosmos
        if cosmos_y >=640:
            cosmos_y = 0
        if background_y >=640:
            background_y = 0
        
        #Fondo
        screen.blit(background, (0,background_y))
        screen.blit(background, (0, background_y - 640))
        screen.blit(cosmos, (0,cosmos_y))
        screen.blit(cosmos, (0, cosmos_y - 640))
        
        #Fondo botones
        screen.blit(logo, logo_rect.topleft)
                
        if play_hovered:
            screen.blit(play_on, play_rect.topleft)
        else:
            screen.blit(play_off, play_rect.topleft)
            
        if quit_hovered:
            screen.blit(quit_on, quit_rect.topleft)
        else:
            screen.blit(quit_off, quit_rect.topleft)
            
        if control_hovered:
            screen.blit(control_on, control_rect.topleft)
        else:
            screen.blit(control_off, control_rect.topleft)
            
            #----------
            
        #-------SONIDO-------
        #Sonido botones
        if play_hovered and not play_hovered_old:
                boton.play()
        if quit_hovered and not quit_hovered_old:
                boton.play()
        if control_hovered and not control_hovered_old:
                boton.play()
        
        #Actualizo los sonidos
        play_hovered_old = play_hovered
        quit_hovered_old = quit_hovered
        control_hovered_old = control_hovered

        #Actualizo la pantalla
        pygame.display.flip()
        clock.tick(60)