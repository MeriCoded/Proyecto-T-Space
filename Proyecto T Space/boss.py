from random import randint
import pygame
import math

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, delay_ms, max_health, bullet_group, settings):
        super().__init__()
        self.image = pygame.image.load("assets/Boss/boss2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (360, 150))
        self.rect = self.image.get_rect(center=(180, 23))
        self.settings = settings
        self.visible = False
        self.delay = delay_ms
        self.start_time = pygame.time.get_ticks()
        self.health = max_health
        self.max_health = max_health
        self.alive = True
        self.bullet_group = bullet_group
        self.pattern_index = 0

        self.last_shot_time = 0
        self.shot_delay = 2000
        
        self.target_y = 23
        self.entering = False

    def update(self):
        current_time = pygame.time.get_ticks()
        if not self.visible and current_time - self.start_time >= self.delay:
            self.visible = True
            self.entering = True
            self.rect.centery = -75

        if self.entering and self.visible:
            if self.rect.centery < self.target_y:
                self.rect.centery += 1
            else:
                self.rect.centery = self.target_y
                self.entering = False

        if self.health <= 0:
            self.alive = False
            self.visible = False

        if self.visible and self.alive and not self.entering:
            if current_time - self.last_shot_time > self.shot_delay:
                self.shooting_pattern()
                self.last_shot_time = current_time

    def draw(self, screen):
        if self.visible and self.alive:
            screen.blit(self.image, self.rect)
            self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        bar_width = 60
        bar_height = 8
        bar_x = self.rect.centerx - bar_width // 2
        bar_y = self.rect.bottom -95
    
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        
        health_percentage = self.health / self.max_health
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, bar_width * health_percentage, bar_height))

        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 2)

    def take_damage(self, damage):
        if self.visible and self.alive:
            self.health -= damage
            print(f"Boss health: {self.health}")

    def shooting_pattern(self):
        if self.pattern_index == 0:
            self.circular_shot()
        elif self.pattern_index == 1:
            self.spiral_shot()
        elif self.pattern_index == 2:
            self.fan_shot()
        elif self.pattern_index == 3:
            self.cross_shot()
        elif self.pattern_index == 4:
            self.wave_shot()
        elif self.pattern_index == 5:
            self.scatter_shot()

        self.pattern_index = (self.pattern_index + 1) % 6

    def circular_shot(self):
        amount = 20
        origin_x = self.rect.centerx
        origin_y = self.rect.bottom - 20

        for i in range(amount):
            angle = math.radians(i * (360 / amount))
            direction = pygame.Vector2(math.cos(angle), math.sin(angle))
            bullet = BossBullet(origin_x, origin_y, direction, speed=3, settings=self.settings)
            self.bullet_group.add(bullet)

    def spiral_shot(self):
        amount = 20
        origin_x = self.rect.centerx
        origin_y = self.rect.bottom - 20
        time_offset = pygame.time.get_ticks() // 10
        for i in range(amount):
            angle = math.radians(i * (360 / amount) + time_offset % 360)
            direction = pygame.Vector2(math.cos(angle), math.sin(angle))
            bullet = BossBullet(origin_x, origin_y, direction, speed=3, settings=self.settings)
            self.bullet_group.add(bullet)

    def fan_shot(self):
        origin_x = self.rect.centerx
        origin_y = self.rect.bottom
        angles = [-30, -20, -10, 0, 10, 20, 30]

        for angle in angles:
            rad = math.radians(angle)
            direction = pygame.Vector2(math.sin(rad), math.cos(rad))
            bullet = BossBullet(origin_x, origin_y, direction, speed=5, settings=self.settings)
            self.bullet_group.add(bullet)

    def cross_shot(self):
        origin_x = self.rect.centerx
        origin_y = self.rect.bottom - 20
        directions = [
            pygame.Vector2(0, -1), 
            pygame.Vector2(0, 1),  
            pygame.Vector2(-1, 0),  
            pygame.Vector2(1, 0)    
        ]
        for direction in directions:
            bullet = BossBullet(origin_x, origin_y, direction, speed=4, settings=self.settings)
            self.bullet_group.add(bullet)

    def wave_shot(self):
        origin_x = self.rect.centerx
        origin_y = self.rect.bottom - 20
        num_bullets = 15
        base_angle = math.radians(90)
        amplitude = math.radians(45)  
        frequency = 2 

        for i in range(num_bullets):
            angle = base_angle + amplitude * math.sin(frequency * i / num_bullets * math.pi)
            direction = pygame.Vector2(math.cos(angle), math.sin(angle))
            bullet = BossBullet(origin_x, origin_y, direction, speed=3, settings=self.settings)
            self.bullet_group.add(bullet)

    def scatter_shot(self):
        origin_x = self.rect.centerx
        origin_y = self.rect.bottom - 20
        num_bullets = 25
        for _ in range(num_bullets):
            angle = math.radians(randint(45, 135))
            direction = pygame.Vector2(math.cos(angle), math.sin(angle)).normalize()
            bullet = BossBullet(origin_x, origin_y, direction, speed=randint(2, 5), settings=self.settings)
            self.bullet_group.add(bullet)
            
class BossBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, settings):
        super().__init__()
        self.image = pygame.image.load("assets/Boss/boss_bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (12, 12))
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction.normalize()
        self.speed = speed
        self.settings = settings

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        if (
            self.rect.top > self.settings.screen_height or
            self.rect.bottom < 0 or
            self.rect.left < 0 or
            self.rect.right > self.settings.screen_width
        ):
            self.kill()
    