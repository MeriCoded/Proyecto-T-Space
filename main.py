import sys
import pygame
from random import randint
from settings import Settings
from estelar import Estelar
from meteor import *
from space import Space
from constants import *
from boss import *
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
        self.boss = Boss(180, 23, delay_ms=300000, max_health=500, bullet_group=self.enemy_bullets, settings=self.settings)

        self.game_over = False

        load_meteor_images()

        self.start_time = None

    def get_meteor_type(self):
        if self.start_time is None:
            return "M1"  # O el tipo por defecto
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        if elapsed_time < M2_TIME:
            return "M1"
        elif elapsed_time < M3_TIME:
            return "M2"
        elif elapsed_time < M4_TIME:
            return "M3"
        else:
            return "M4"
    
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
                        Meteor(tipo, (x, y), (self.meteors_grandes,))
                    self.last_meteor_time = current_time

                self.estelar.update_estelar()
                self.bullets.update()
                self.meteors_grandes.update(delta_time)
                self.enemy_bullets.update()
                self.boss.update()
                self.space.draw()
                self.enemy_bullets.draw(self.screen)
                self.boss.draw(self.screen)

                for bullet in self.bullets.sprites():
                    if self.boss.visible and self.boss.alive and bullet.rect.colliderect(self.boss.rect):
                        self.boss.take_damage(1)
                        bullet.kill()

                self.meteors_grandes.update(delta_time)
                
                # Colisiones - Entre balas y meteoritos
                hits = pygame.sprite.groupcollide(self.meteors_grandes, self.bullets, True, True)

                for meteor in hits:
                    meteor.break_apart((self.meteors_grandes,))
                    if meteor.tipo == "M1":
                        self.score += 10
                    elif meteor.tipo == "M2":
                        self.score += 30
                    elif meteor.tipo == "M3":
                        self.score += 60
                    elif meteor.tipo == "M4":
                        self.score += 80
                
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

                if not self.boss.alive and self.boss.visible == False:
                    ganar = victory()
                    if ganar == "retry":
                        self. reset_game()
                    else:
                        running = False 

                pygame.display.flip()

            else:
                perder = gameover()
                if perder == "retry":
                    self.reset_game()
                else:
                    running = False

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    menu()
    while True:
        ventana = Window()
        ventana.run()