import sys

import pygame
import time
import math


from settings import Settings
from estelar import Estelar
from alien import Alien
from space import Space

class Window:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Touhou pero con navecitas")
        self.clock = pygame.time.Clock()
        self.screen_rect = self.screen.get_rect()
        self.estelar = Estelar(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.space = Space(self.screen, self.settings)

        for i in range(4):
            alien = Alien(self, 40 + i*70, 100)
            self.aliens.add(alien)

    def run(self):
        running = True
        

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.estelar.update_estelar()
            self.bullets.update()
            self.aliens.update()
            self.space.draw()

            pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)

            self.estelar.draw_estelar()
            self.bullets.draw(self.screen)
            for bullet in self.bullets:
                bullet.draw_bullet()
            self.aliens.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.settings.fps)



            
        
        pygame.quit()
        sys.exit()



if __name__ == "__main__":
    ventana = Window()
    ventana.run()