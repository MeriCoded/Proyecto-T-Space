import sys

import pygame

from settings import Settings
from estelar import Estelar

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

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill(self.settings.bg_color)

            self.estelar.update_estelar()
            self.estelar.draw_estelar()

            pygame.display.flip()
            self.clock.tick(self.settings.fps)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    ventana = Window()
    ventana.run()