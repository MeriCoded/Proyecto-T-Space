import sys
import pygame
from random import randint
from settings import Settings
from estelar import Estelar
from meteor import *
from space import Space
from constants import *
from boss import *
from boss_alert import *
from menu import menu
from controles import controles
from gameover import gameover
from victory import victory

class Window:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Estelar’s adventure: Space battle")
        self.clock = pygame.time.Clock()
        self.screen_rect = self.screen.get_rect()
        self.score = 0
        self.estelar = Estelar(self)
        self.bullets = pygame.sprite.Group()
        self.space = Space(self.screen, self.settings)
        self.meteors_grandes = pygame.sprite.Group()
        self.last_meteor_time = pygame.time.get_ticks()
        self.meteor_delay = 400
        self.enemy_bullets = pygame.sprite.Group()
        self.boss = Boss(100, 23, delay_ms=90000, max_health=150, bullet_group=self.enemy_bullets, settings=self.settings)
        alert_delay_ms = self.boss.delay - 7000 
        self.boss_alert = BossAlert(self.settings.screen_width // 2, self.settings.screen_height // 4, delay_ms=alert_delay_ms, settings=self.settings)
        self.game_over = False
        self.start_time = None

    def get_meteor_type(self):
        if self.start_time is None:
            return "M1"  # O el tipo por defecto
        current_ticks = pygame.time.get_ticks()
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        print(f"Start Time: {self.start_time}, Current Ticks: {current_ticks}, Elapsed Time: {elapsed_time}s")
        if elapsed_time < M2_TIME:
            return "M1"
        elif elapsed_time < M3_TIME:
            return "M2"
        elif elapsed_time < M4_TIME:
            return "M3"
        elif elapsed_time < M5_TIME:
            return "M4"
        else:
            return "M5"
    
    # Función para agregar las vidas de Estelar en pantalla    
    def draw_lifes(self):
        life_icon = pygame.transform.scale(pygame.image.load("Assets/Player/life_icon.png"), (40, 40))
        icon_width = life_icon.get_width()
        icon_height = life_icon.get_height()

        for i in range(self.estelar.lifes):
            x = self.settings.screen_width - (i + 1) * (icon_width - 5) - 5  # de derecha a izquierda
            y = self.settings.screen_height - icon_height - 5  # margen inferior
            self.screen.blit(life_icon, (x, y))

    def reset_game(self):
        self.__init__()  # Reinicia el juego desde cero

    def run(self):
        self.start_time = pygame.time.get_ticks()  # El contador empieza aquí
        running = True

        while running:
            delta_time = self.clock.tick(self.settings.fps) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.game_over:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_meteor_time > self.meteor_delay:
                    if len(self.meteors_grandes) < 30:
                        tipo = self.get_meteor_type()
                        x = randint(0, self.settings.screen_width)
                        y = randint(-200, -100)
                        create_meteor(tipo, (x, y), (self.meteors_grandes,))
                    self.last_meteor_time = current_time

                self.estelar.update_estelar()
                self.bullets.update()
                self.meteors_grandes.update(delta_time)
                self.enemy_bullets.update()
                self.boss.update()
                self.boss_alert.update(current_time) 
                self.space.draw()
                self.enemy_bullets.draw(self.screen)
                self.boss.draw(self.screen)

                if self.boss_alert.visible and not self.boss.visible:
                    self.boss_alert.play_sound_once()
                elif self.boss.visible: # Si el jefe es visible, detener y detener el sonido de la alerta
                    self.boss_alert.stop_sound()

                for bullet in self.bullets.sprites():
                    if self.boss.visible and self.boss.alive and bullet.rect.colliderect(self.boss.rect):
                        self.boss.take_damage(1)
                        bullet.kill()

                self.meteors_grandes.update(delta_time)
                
                # Colisiones - Entre balas y meteoritos
                hits = pygame.sprite.groupcollide(self.meteors_grandes, self.bullets, True, True)

                for meteor in hits:
                    meteor.break_apart((self.meteors_grandes,))
                    self.score += meteor.get_points()
                    print(self.score)
                    
                # Colisiones - Entre Estelar y los meteoritos
                collided_meteors = pygame.sprite.spritecollide(self.estelar, self.meteors_grandes, True, pygame.sprite.collide_mask)
                collided_bullets = pygame.sprite.spritecollide(self.estelar, self.enemy_bullets, True, pygame.sprite.collide_mask)

                if collided_meteors or collided_bullets:
                    self.estelar.lifes -= 1
                    print(f"¡Estelar ha perdido una vida! Vidas restantes: {self.estelar.lifes}")
                    if self.estelar.lifes <= 0:
                            self.game_over = True

                self.draw_lifes()
                self.estelar.draw_estelar()
                self.bullets.draw(self.screen)
                self.enemy_bullets.draw(self.screen)
                for bullet in self.bullets:
                    bullet.draw_bullet()
                self.meteors_grandes.draw(self.screen)
                if self.boss_alert.visible and not self.boss.visible:
                    self.boss_alert.draw(self.screen)
                if not self.boss.alive and self.boss.visible == False:
                    ganar = victory(self.score)
                    if ganar == "retry":
                        return "retry"
                    else:
                        running = False
                        return "quit"

                pygame.display.flip()

            else:
                perder = gameover(self.score)
                if perder == "retry":
                    return "retry"  
                else:
                    running = False
                    return "quit"

if __name__ == "__main__":
    menu()
    while True:
        ventana = Window()
        resultado_run = ventana.run()

        if resultado_run == "quit":
            break

pygame.quit()
sys.exit()