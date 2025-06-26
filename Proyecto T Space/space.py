import pygame
import math

from settings import Settings

class Space:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.bg_images = []
        for i in range(1, 4):
            bg_image = pygame.image.load(f"Assets/Espacio/bg{i}.png").convert_alpha()
            self.bg_images.append(bg_image)
        self.bg_height = self.bg_images[0].get_height()
        
        self.speeds = [4, 3, 1] 
        self.offsets = [0, 0, 0]

    def draw(self):
        bg_loop = math.ceil(self.settings.screen_height / self.bg_height) + 1
        for idx, bg in enumerate(self.bg_images):
            for i in range(bg_loop):
                y = (i * self.bg_height + self.offsets[idx]) % (self.bg_height * bg_loop) - self.bg_height
                self.screen.blit(bg, (0, y))
            self.offsets[idx] = (self.offsets[idx] + self.speeds[idx]) % self.bg_height
