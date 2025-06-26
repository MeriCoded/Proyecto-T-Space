def controles():
    import pygame, sys
    pygame.init()
    pygame.mixer.init()
    size = (360,640)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    background = pygame.image.load("Assets/Espacio/bg1.png")
    cosmos = pygame.image.load("Assets/Espacio/bg4.png")
    flechas = pygame.image.load("Assets/Controles/flechas.png")
    spacebar = pygame.image.load("Assets/Controles/barra.png")
    esc_off = pygame.image.load("Assets/Controles/esc_off.png")
    esc_on = pygame.image.load("Assets/Controles/esc_on.png")

    flechas = pygame.transform.scale(flechas,(180,120))
    spacebar = pygame.transform.scale(spacebar,(200,80))
    esc_off = pygame.transform.scale(esc_off,(47,34))
    esc_on = pygame.transform.scale(esc_on,(47,34))
    
    esc_rect = esc_off.get_rect(center=(size[0]// 9, 40))

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("Assets/Sonidos/beat.wav")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
    pygame.mixer.Sound("Assets/Sonidos/boton1.wav")
    boton = pygame.mixer.Sound("Assets/Sonidos/boton1.wav")
    boton.set_volume(0.3)
  
    esc_hovered_old = False

    cosmos_y = 0
    velocidad_cosmos = 2
    background_y = 0
    velocidad_backgound = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if esc_rect.collidepoint(event.pos):
                    return
        mouse_pos = pygame.mouse.get_pos()

        esc_hovered = esc_rect.collidepoint(mouse_pos)
        
        background_y += velocidad_backgound
        cosmos_y += velocidad_cosmos
        if cosmos_y >=640:
            cosmos_y = 0
        if background_y >=640:
            background_y = 0

        screen.blit(background, (0,background_y))
        screen.blit(background, (0, background_y - 640))
        screen.blit(cosmos, (0,cosmos_y))
        screen.blit(cosmos, (0, cosmos_y - 640))
        screen.blit(flechas, [93,160])
        screen.blit(spacebar, [84,400])
        
        if esc_hovered:
            screen.blit(esc_on, esc_rect.topleft)
        else:
            screen.blit(esc_off, esc_rect.topleft)
            
        if esc_hovered and not esc_hovered_old:
            boton.play()

        esc_hovered_old = esc_hovered

        font = pygame.font.SysFont("Fonts/Oxanium-Bold.ttf", 35)
        mover = font.render("CONTROLES", True, (255, 215, 0))
        disparar = font.render("DISPARAR", True, (255, 215, 0))
        
        mover_text = mover.get_rect(topleft=(104,130))
        disparar_text = disparar.get_rect(topleft=(119,370))
        screen.blit(mover, mover_text)
        screen.blit(disparar, disparar_text)
        
        pygame.display.flip()

        pygame.display.flip()
        clock.tick(60)