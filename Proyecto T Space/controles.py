def controles():
    import pygame, sys
    pygame.init()
    pygame.mixer.init()
    size = (360,640)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    #-----IMAGENES-----
    #Cargar imagenes
    fondo = pygame.image.load("Assets/Espacio/bg1.png")
    cosmos = pygame.image.load("Assets/Espacio/bg4.png")
    flechas = pygame.image.load("Assets/Controles/flechas.png")
    barra = pygame.image.load("Assets/Controles/barra.png")
    esc_apagado = pygame.image.load("Assets/Controles/esc_apagado.png")
    esc_brillo = pygame.image.load("Assets/Controles/esc_brillo.png")
    esc_apagado = pygame.image.load("Assets/Menu/esc_apagado.png")
    esc_brillo = pygame.image.load("Assets/Menu/esc_brillo.png")


    #Escalar imagenes
    flechas = pygame.transform.scale(flechas,(180,120))
    barra = pygame.transform.scale(barra,(200,80))
    esc_apagado = pygame.transform.scale(esc_apagado,(47,34))
    esc_brillo = pygame.transform.scale(esc_brillo,(47,34))
    
    
    #Posición imagen
    esc_rect = esc_apagado.get_rect(center=(size[0]// 9, 40))

    #-------SONIDO-------
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("Assets/Sonidos/beat.wav")
        pygame.mixer.music.set_volume(0.2) #Ajustar en base al audio final
        pygame.mixer.music.play(-1)
    pygame.mixer.Sound("Assets/Sonidos/boton1.wav")
    boton = pygame.mixer.Sound("Assets/Sonidos/boton1.wav")
    boton.set_volume(0.5) #Ajustar en base al audio final
    
    #Sonido botones
    esc_hovered_old = False

    #Velocidad
    cosmos_y = 0
    velocidad_cosmos = 2
    fondo_y = 0
    velocidad_fondo = 1

    while True:
        #Ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if esc_rect.collidepoint(event.pos):
                    return
        #Mouse
        mouse_pos = pygame.mouse.get_pos()
        
        #Colisión boton
        esc_hovered = esc_rect.collidepoint(mouse_pos)
        
                
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
        screen.blit(flechas, [93,160])
        screen.blit(barra, [84,400])
        
        if esc_hovered:
            screen.blit(esc_brillo, esc_rect.topleft)
        else:
            screen.blit(esc_apagado, esc_rect.topleft)
            
            #----------
        
        #-------SONIDO-------
        #Sonido boton
        if esc_hovered and not esc_hovered_old:
            boton.play()
        
        #Actualizo sonido
        esc_hovered_old = esc_hovered
            #----------
        
        #-------TEXTO-------
        font = pygame.font.SysFont("Fonts/Oxanium-Bold.ttf", 35)
        mover = font.render("CONTROLES", True, (255, 215, 0))
        disparar = font.render("DISPARAR", True, (255, 215, 0))
        
        mover_text = mover.get_rect(topleft=(104,130))
        disparar_text = disparar.get_rect(topleft=(119,370))
        screen.blit(mover, mover_text)
        screen.blit(disparar, disparar_text)
        
        pygame.display.flip()

        #Actualizo la pantalla
        pygame.display.flip()
        clock.tick(60)