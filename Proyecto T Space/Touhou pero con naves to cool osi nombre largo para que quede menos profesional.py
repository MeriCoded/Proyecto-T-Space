import sys

import pygame
import time

from settings import Settings
from estelar import Estelar
from alien import Alien

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
        # Crea algunos enemigos de ejemplo
        for i in range(10):
            alien = Alien(self, 100 + i*80, 100)
            self.aliens.add(alien)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill(self.settings.bg_color)

            self.estelar.update_estelar()
            self.bullets.update()
            self.aliens.update()

            #            import pygame
            
            class Alien(pygame.sprite.Sprite):
                def __init__(self, game, x, y):
                    super().__init__()
                    self.game = game
                    self.image = pygame.Surface((40, 30))
                    self.image.fill((0, 200, 0))
                    self.rect = self.image.get_rect()
                    self.rect.x = x
                    self.rect.y = y
            
                def update(self):
                    # Puedes agregar movimiento aquí si quieres
                    pass
            hits = pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)

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