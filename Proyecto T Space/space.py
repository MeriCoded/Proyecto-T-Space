import pygame
import math

from settings import Settings

class Space:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.bg = pygame.image.load("assets/Espacio/bg1.png").convert()
        self.bg_height = self.bg.get_height()
        self.scroll_speed = 0

    def draw(self):
        bg_loop = math.ceil(self.settings.screen_height / self.bg_height) + 1
        for i in range(bg_loop):
            y = (i * self.bg_height + self.scroll_speed) % (self.bg_height * bg_loop) - self.bg_height
            self.screen.blit(self.bg, (0, y))

        self.scroll_speed += 5
        if self.scroll_speed >= self.bg_height:
            self.scroll_speed = 0
