import pygame
from settings import Settings

class Alien(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        aliencito = pygame.image.load("assets/Enemigos/Alien.png").convert_alpha()
        self.image = pygame.transform.scale(aliencito, (40, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

