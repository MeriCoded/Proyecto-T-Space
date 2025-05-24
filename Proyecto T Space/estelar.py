import pygame

from settings import Settings

class Estelar(pygame.sprite.Sprite):
    #La nave se llamara Estelar
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/estelar.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.WIDTH // 2
        self.rect.bottom = Settings.HEIGHT - 10
        self.speed = 5