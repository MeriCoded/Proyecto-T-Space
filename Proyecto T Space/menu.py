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
    fondo = pygame.image.load("Assets/Espacio/bg1.png")
    cosmos = pygame.image.load("Assets/Espacio/bg4.png")
    logo = pygame.image.load("Assets/Menu/logo.png")
    play_apagado = pygame.image.load("Assets/Menu/play_apagado.png")
    play_brillo = pygame.image.load("Assets/Menu/play_brillo.png")
    quit_apagado = pygame.image.load("Assets/Menu/quit_apagado.png")
    quit_brillo = pygame.image.load("Assets/Menu/quit_brillo.png")
    control_apagado = pygame.image.load("Assets/Menu/control_apagado.png")
    control_brillo = pygame.image.load("Assets/Menu/control_brillo.png")


    #Escalar imagenes
    logo = pygame.transform.scale(logo,(290,110))
    play_apagado = pygame.transform.scale(play_apagado,(150,60))
    play_brillo = pygame.transform.scale(play_brillo,(150,60))
    quit_apagado = pygame.transform.scale(quit_apagado,(150,60))
    quit_brillo = pygame.transform.scale(quit_brillo,(150,60))
    control_apagado = pygame.transform.scale(control_apagado,(47,34))
    control_brillo = pygame.transform.scale(control_brillo,(47,34))

    #posición imagenes
    logo_rect = logo.get_rect(center=(size[0]//2,200))
    play_rect = play_apagado.get_rect(center=(size[0]//2,350))
    quit_rect = quit_apagado.get_rect(center=(size[0]//2,450))
    control_rect = control_apagado.get_rect(center=(size[0]//9,40))

    #Velocidad fondo
    cosmos_y = 0
    velocidad_cosmos = 2
    fondo_y = 0
    velocidad_fondo = 1

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
        
        #Fondo botones
        screen.blit(logo, logo_rect.topleft)
                
        if play_hovered:
            screen.blit(play_brillo, play_rect.topleft)
        else:
            screen.blit(play_apagado, play_rect.topleft)
            
        if quit_hovered:
            screen.blit(quit_brillo, quit_rect.topleft)
        else:
            screen.blit(quit_apagado, quit_rect.topleft)
            
        if control_hovered:
            screen.blit(control_brillo, control_rect.topleft)
        else:
            screen.blit(control_apagado, control_rect.topleft)
            
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