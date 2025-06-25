def victory (score):
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
    victory = pygame.image.load("Assets/Victory/you_win.png")
    play_again_off = pygame.image.load("Assets/Victory/play_again_off.png")
    play_again_on = pygame.image.load("Assets/Victory/play_again_on.png")
    quit_off = pygame.image.load("Assets/Victory/quit_off.png")
    quit_on = pygame.image.load("Assets/Victory/quit_on.png")

    #Escalar imagenes
    victory = pygame.transform.scale(victory,(260,190))
    play_again_off = pygame.transform.scale(play_again_off,(150,80))
    play_again_on = pygame.transform.scale(play_again_on,(150,80))
    quit_off = pygame.transform.scale(quit_off,(120,35))
    quit_on = pygame.transform.scale(quit_on,(120,35))

    #posición imagenes
    victory_rect =victory.get_rect(center=(size[0]//2,180))
    play_again_rect = play_again_off.get_rect(center=(size[0]//2,380))
    quit_rect = quit_off.get_rect(center=(size[0]//2,470))

    #Velocidad fondo
    cosmos_y = 0
    velocidad_cosmos = 2
    background_y = 0
    velocidad_background = 1

    #Game Over parpadeante
    mostrar_victory = True
    tiempo_parpadeo = 350
    ultimo_cambio = pygame.time.get_ticks()

    #"Score" parpadeante
    font = pygame.font.Font("Fonts/Oxanium-Bold.ttf", 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(size[0]//2, 300))

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
                if play_again_rect.collidepoint(event.pos):
                    return "retry"
                elif quit_rect.collidepoint(event.pos):
                    sys.exit()
                #----------
                
        #Mouse
        mouse_pos = pygame.mouse.get_pos()
        play_again_hovered = play_again_rect.collidepoint(mouse_pos)
        quit_hovered = quit_rect.collidepoint(mouse_pos)
                    
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
                
        #Game over
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultimo_cambio >= tiempo_parpadeo:
            mostrar_victory = not mostrar_victory
            ultimo_cambio = tiempo_actual
            
        if mostrar_victory:
            screen.blit(victory, victory_rect.topleft)
            screen.blit(score_text, score_rect.topleft)
            
        #Botones
        if play_again_hovered:
            screen.blit(play_again_on, play_again_rect.topleft)
        else:
            screen.blit(play_again_off, play_again_rect.topleft)
                
        if quit_hovered:
            screen.blit(quit_on, quit_rect.topleft)
        else:
            screen.blit(quit_off, quit_rect.topleft)
                
            #----------
                
        #-------SONIDO-------
        #Sonido botones
        if play_again_hovered and not retry_hovered_old:
            boton.play()
        if quit_hovered and not quit_hovered_old:
            boton.play()
            
        #Actualizo los sonidos
        retry_hovered_old = play_again_hovered
        quit_hovered_old = quit_hovered
        
        #Actualizo la pantalla
        pygame.display.flip()
        clock.tick(60)