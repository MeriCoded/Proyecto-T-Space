def gameover(score):
    import pygame, sys
    from controles import controles
    pygame.init()
    pygame.mixer.init()
    size = (360,640)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Estelar’s adventure: Space battle")

    background = pygame.image.load("Assets/Espacio/bg1.png")
    cosmos = pygame.image.load("Assets/Espacio/bg4.png")
    gameover = pygame.image.load("Assets/Gameover/game_over.png")
    retry_off = pygame.image.load("Assets/Gameover/retry_apagado.png")
    retry_on = pygame.image.load("Assets/Gameover/retry_brillo.png")
    quit_off = pygame.image.load("Assets/Gameover/quit_apagado.png")
    quit_on = pygame.image.load("Assets/Gameover/quit_brillo.png")

    gameover = pygame.transform.scale(gameover,(250,110))
    retry_off = pygame.transform.scale(retry_off,(150,40))
    retry_on = pygame.transform.scale(retry_on,(150,40))
    quit_off = pygame.transform.scale(quit_off,(120,40))
    quit_on = pygame.transform.scale(quit_on,(120,40))

    gameover_rect = gameover.get_rect(center=(size[0]//2,200))
    retry_rect = retry_off.get_rect(center=(size[0]//2,350))
    quit_rect = quit_off.get_rect(center=(size[0]//2,450))

    cosmos_y = 0
    velocidad_cosmos = 2
    background_y = 0
    velocidad_backgound = 1

    mostrar_gameover = True
    tiempo_parpadeo = 350
    ultimo_cambio = pygame.time.get_ticks()

    font = pygame.font.Font("Fonts/Oxanium-Bold.ttf", 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(size[0]//2, 280))


    boton = pygame.mixer.Sound("Assets/Sonidos/boton2.wav")
    boton.set_volume(0.5)

    retry_hovered_old = False
    quit_hovered_old = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    return "retry"
                elif quit_rect.collidepoint(event.pos):
                    return "quit"

        mouse_pos = pygame.mouse.get_pos()
        retry_hovered = retry_rect.collidepoint(mouse_pos)
        quit_hovered = quit_rect.collidepoint(mouse_pos)
                
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
            
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultimo_cambio >= tiempo_parpadeo:
            mostrar_gameover = not mostrar_gameover
            ultimo_cambio = tiempo_actual
            
        if mostrar_gameover:
            screen.blit(gameover, gameover_rect.topleft)
            screen.blit(score_text, score_rect.topleft)

        if retry_hovered:
            screen.blit(retry_on, retry_rect.topleft)
        else:
            screen.blit(retry_off, retry_rect.topleft)
                
        if quit_hovered:
            screen.blit(quit_on, quit_rect.topleft)
        else:
            screen.blit(quit_off, quit_rect.topleft)
                
        if retry_hovered and not retry_hovered_old:
            boton.play()
        if quit_hovered and not quit_hovered_old:
            boton.play()

        retry_hovered_old = retry_hovered
        quit_hovered_old = quit_hovered

        pygame.display.flip()
        clock.tick(60)