import pygame
from settings import *
import math

class Boss:
    def __init__(self,x,y, delay_ms, max_health):
        self.image = pygame.Surface((40, 30))
        self.image.fill((255, 55, 80))
        self.rect = self.image.get_rect()
        
        self.visible = False
        self.delay = delay_ms
        self.start_time = pygame.time.get_ticks()
        self.health = max_health
        self.alive = True  # Para saber si el boss sigue vivo
        self.speed = 4
        self.direction = 1
    
    def update(self):
        current_time = pygame.time.get_ticks()
        if not self.visible and current_time - self.start_time >= self.delay:
            self.visible = True  # Después del delay, lo hacemos visible
        if self.health <= 0:
            self.alive = False
            self.visible = False  # Deja de mostrarse    
        self.rect.x += self.speed * self.direction
        if self.rect.right > 360 - 20:
            self.direction = -1
        elif self.rect.left < 20:
            self.direction = 1
    
    def draw(self, screen):
        if self.visible and self.alive:
         pygame.draw.rect(screen, (255, 55, 80), self.rect)
    
    def take_damage(self, damage):
        if self.visible and self.alive:
            self.health -= 3
            print(f"Boss health: {self.health}")    