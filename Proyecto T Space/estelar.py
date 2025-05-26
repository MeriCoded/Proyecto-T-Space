import pygame
import time

from settings import Settings

class Estelar(pygame.sprite.Sprite):
    #La nave se llamara Estelar
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((40, 30))  # Tamaño de la nave
        self.image.fill((255, 55, 80))      # Color de la nave
        self.rect = self.image.get_rect()
        self.rect.centerx = game.settings.screen_width // 2
        self.rect.bottom = game.settings.screen_height - 10
        self.speed = 5
        self.direction = pygame.math.Vector2(0, 0)
        self.shoot_cooldown = 0
        self.burst_count = 0
        self.burst_timer = 0

    def draw_estelar(self):
        pygame.draw.rect(self.game.screen, (255, 55, 80), self.rect)

    def update_estelar(self):
        self.input()
        self.move()
        self.handle_burst()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
              self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
              self.direction.x = 0
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0 and self.burst_count == 0:
                self.burst_count = 3  # de cuanto quiero la rafaga
                self.burst_timer = 0

    def handle_burst(self):
        if self.burst_count > 0:
            if self.burst_timer <= 0:
                self.shoot()
                self.burst_count -= 1
                self.burst_timer = 7  # frames entre balas
            else:
                self.burst_timer -= 1
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self):
        if self.direction.x and self.direction.y:
            self.direction.normalize_ip()
        self.rect.x += self.direction.x * self.game.settings.estelar_speed
        self.rect.y += self.direction.y * self.game.settings.estelar_speed
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.game.settings.screen_width:
            self.rect.right = self.game.settings.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.game.settings.screen_height:
            self.rect.bottom = self.game.settings.screen_height

    def shoot(self):
        bullet = Bullet(self.game, self.rect.centerx, self.rect.top)
        self.game.bullets.add(bullet)
        if self.burst_count == 1:
            self.shoot_cooldown = 15  # cooldown entre ráfagas para que no sea tremendo spam (temporal)

import pygame.sprite
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = game.settings.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.game.screen, (255, 255, 0), self.rect)
    


    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()  # Elimina las balitas