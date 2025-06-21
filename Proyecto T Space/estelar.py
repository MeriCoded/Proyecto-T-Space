import pygame
import time

from settings import Settings

class Estelar(pygame.sprite.Sprite):
    #La nave se llamara Estelar
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Assets/Player/Estelar.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 60))
        self.rect = self.image.get_rect()
        self.rect.centerx = game.settings.screen_width // 2
        self.rect.bottom = game.settings.screen_height - 10
        self.speed = 5
        self.direction = pygame.math.Vector2(0, 0)
        self.shoot_cooldown = 0
        self.burst_count = 0
        self.burst_timer = 0
        # Utilizamos mascaras para generar colisiones pixel-perfect
        #self.mask = pygame.mask.from_surface(self.image) - No es necesario escribirlo

    def draw_estelar(self):
        self.game.screen.blit(self.image, self.rect)

    def update_estelar(self):
        self.input()
        self.move()
        self.handle_burst()

        #Controles
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        
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
        self.image = pygame.image.load("Assets/Player/Bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 10))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = game.settings.bullet_speed
        #self.mask = pygame.mask.from_surface(self.image) - No es necesario escribirlo

    def draw_bullet(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()  # Elimina las balitas