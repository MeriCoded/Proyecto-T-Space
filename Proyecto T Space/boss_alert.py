import pygame

class BossAlert(pygame.sprite.Sprite):
    def __init__(self, x, y, delay_ms, settings):
        super().__init__()
        self.settings = settings
        self.delay = delay_ms  # Tiempo en milisegundos hasta que la alerta se vuelve visible
        self.start_time = pygame.time.get_ticks() # Se establecerá al iniciar el juego
        self.visible = False # La alerta no es visible al principio

        # Cargar la imagen del símbolo de exclamación
        self.image = pygame.image.load("Assets/Boss/BossAlert.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80)) # Ajusta el tamaño

        if self.image:
            self.rect = self.image.get_rect(center=(x, y))
        else:
            self.rect = pygame.Rect(x - 40, y - 40, 80, 80) # Rect placeholder if image fails

        # Cargar sonido de alerta
        self.sound_played = False
        self.alert_sound = pygame.mixer.Sound("Assets/Sonidos/BossAlert.mp3")
        self.alert_sound.set_volume(0.3)

        # Variables para el parpadeo
        self.flash_interval = 100 # Intervalo de parpadeo en ms
        self.last_flash_time = 0
        self.show_icon = True

    def update(self, current_game_time):
        # La alerta se vuelve visible cuando el tiempo del juego alcanza su delay
        if not self.visible and current_game_time >= self.delay:
            self.visible = True
            
        # Lógica de parpadeo si la alerta es visible
        if self.visible:
            if current_game_time - self.last_flash_time > self.flash_interval:
                self.show_icon = not self.show_icon
                self.last_flash_time = current_game_time

    def draw(self, screen):
        if self.visible and self.show_icon and self.image:
            screen.blit(self.image, self.rect)
    
    def play_sound_once(self):
        if not self.sound_played and self.alert_sound:
            self.alert_sound.play()
            self.sound_played = True
            
    def stop_sound(self):
        if self.alert_sound and self.alert_sound.get_num_channels() > 0:
            self.alert_sound.stop()

    def reset(self, new_start_time):
        """Reinicia el estado de la alerta para un nuevo juego."""
        self.start_time = new_start_time
        self.visible = False
        self.sound_played = False
        self.last_flash_time = new_start_time
        self.show_icon = True
        self.stop_sound() # Asegurarse de que el sonido se detenga al resetear
