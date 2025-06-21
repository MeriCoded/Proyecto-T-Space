import sys
import pygame
import time #eliminar si no usamos
import math #eliminar si no usamos
from random import randint
from settings import Settings
from estelar import Estelar
from meteor_v2 import *
from space import Space
from constants import *
from boss import Boss
from menu import menu
from controles import controles

#font = pygame.font.Font('Fonts/Oxanium-Bold.ttf', 20) Posiblemente lo use para el score
#font.render("Font test", True, 'White')

class Window:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Estelar’s adventure: Space battle")
        self.clock = pygame.time.Clock()
        self.screen_rect = self.screen.get_rect()

        self.estelar = Estelar(self)
        self.bullets = pygame.sprite.Group()
        self.space = Space(self.screen, self.settings)
        self.meteors_grandes = pygame.sprite.Group()
        self.last_meteor_time = pygame.time.get_ticks()
        self.meteor_delay = 600

        self.boss = Boss(100, 300, delay_ms=10000, max_health=20)

        self.game_over = False

        load_meteor_images()

    def get_meteor_type(self):
        elapsed_time = pygame.time.get_ticks() // 1000
        if elapsed_time < M2_TIME:
            return "M1"
        elif elapsed_time < M3_TIME:
            return "M2"
        elif elapsed_time < M4_TIME:
            return "M3"
        else:
            return "M4"

    def show_game_over(self):
        font = pygame.font.SysFont("Fonts/Oxanium-Bold.ttf", 25)
        text = font.render("PERDISTE (haga click para reiniciar)", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.settings.screen_width//2, self.settings.screen_height//2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False
                    self.reset_game()

    def reset_game(self):
        self.__init__()  # Reinicia el juego desde cero

    def run(self):
        running = True

        while running:
            delta_time = self.clock.tick(self.settings.fps) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.game_over:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_meteor_time > self.meteor_delay:
                    if len(self.meteors_grandes) < 12:
                        tipo = self.get_meteor_type()
                        x = randint(0, self.settings.screen_width)
                        y = randint(-200, -100)
                        Meteor(tipo, (x, y), (self.meteors_grandes,))
                    self.last_meteor_time = current_time

                self.estelar.update_estelar()
                self.bullets.update()
                self.space.draw()
                self.boss.draw(self.screen)
                self.boss.update()

                for bullet in self.bullets.sprites():
                    if self.boss.visible and self.boss.alive and bullet.rect.colliderect(self.boss.rect):
                        self.boss.take_damage(1)
                        bullet.kill()

                self.meteors_grandes.update(delta_time)
                
                # Colisiones - Entre balas y meteoritos
                pygame.sprite.groupcollide(self.meteors_grandes, self.bullets, True, True)
            
                # Colisiones - Entre Estelar y los meteoritos
                collided_meteors = pygame.sprite.spritecollide(self.estelar, self.meteors_grandes, True, pygame.sprite.collide_mask)

                if collided_meteors:
                    self.game_over = True

                self.estelar.draw_estelar()
                self.bullets.draw(self.screen)
                for bullet in self.bullets:
                    bullet.draw_bullet()
                self.meteors_grandes.draw(self.screen)

                pygame.display.flip()

            else:
                self.show_game_over()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    menu()
    ventana = Window()
    ventana.run()
