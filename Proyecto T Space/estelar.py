import pygame
import time
from constants import *
from settings import Settings

class Estelar(pygame.sprite.Sprite):
    #La nave se llamara Estelar
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Assets/Player/Estelar7.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 70))
        self.rect = self.image.get_rect()
        self.rect.centerx = game.settings.screen_width // 2
        self.rect.bottom = game.settings.screen_height - 10
        self.health = 500
        self.lifes = 5
        self.speed = 5
        self.level = 0
        self.direction = pygame.math.Vector2(0, 0)
        self.shoot_cooldown = 0
        self.burst_count = 0
        self.burst_timer = 0
        self.shoot_sound = pygame.mixer.Sound("Assets/Sonidos/disparo.wav")
        self.shoot_sound.set_volume(0.1)

    def draw_estelar(self):
        self.game.screen.blit(self.image, self.rect)

    def update_estelar(self):
        self.input()
        self.move()
        self.handle_burst()
        
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0 and self.burst_count == 0:
                self.burst_count = 1 
                self.burst_timer = 0

    def handle_burst(self):
        if self.burst_count > 0:
            if self.burst_timer <= 0:
                self.shoot()
                self.burst_count -= 1
                self.burst_timer = 5 
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
        score = self.game.score
        if score >= LEVEL_4:
            level = 4
        elif score >= LEVEL_3:
            level = 3
        elif score >= LEVEL_2:
            level = 2
        else:
            level = 1
        
        if level == 1:
            bullet = Bullet(self.game, self.rect.centerx, self.rect.top)
            self.game.bullets.add(bullet)
        
        elif level == 2:
            bullet1 = Bullet(self.game, self.rect.centerx - 10, self.rect.top)
            bullet2 = Bullet(self.game, self.rect.centerx + 10, self.rect.top)
            self.game.bullets.add(bullet1, bullet2)
            
        elif level == 3:
            bullet1 = Bullet(self.game, self.rect.centerx, self.rect.top)
            bullet2 = Bullet(self.game, self.rect.centerx - 15, self.rect.top + 5)
            bullet3 = Bullet(self.game, self.rect.centerx + 15, self.rect.top + 5)
            self.game.bullets.add(bullet1, bullet2, bullet3)

        elif level == 4:
            bullet1 = Bullet(self.game, self.rect.centerx, self.rect.top)
            bullet2 = Bullet(self.game, self.rect.centerx - 20, self.rect.top + 10)
            bullet3 = Bullet(self.game, self.rect.centerx + 20, self.rect.top + 10)
            bullet4 = Bullet(self.game, self.rect.centerx - 10, self.rect.top) 
            bullet5 = Bullet(self.game, self.rect.centerx + 10, self.rect.top)
            self.game.bullets.add(bullet1, bullet2, bullet3, bullet4, bullet5)
        
        self.shoot_sound.play() 
        if self.burst_count == 1:
            self.shoot_cooldown = 25 
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Assets/Player/Bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 21))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = game.settings.bullet_speed
        self.damage = 10

    def draw_bullet(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()