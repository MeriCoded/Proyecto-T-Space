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
        self.alive = True
        self.bullet_group = bullet_group

        self.last_shot_time = 0
        self.shot_delay = 2000  # Tiempo entre disparos en milisegundos

    def update(self):
        current_time = pygame.time.get_ticks()
        if not self.visible and current_time - self.start_time >= self.delay:
            self.visible = True  # El jefe aparece tras el delay

        if self.health <= 0:
            self.alive = False
            self.visible = False  # Deja de mostrarse si muere

        if self.visible and self.alive:
            if current_time - self.last_shot_time > self.shot_delay:
                self.shooting_pattern()
                self.last_shot_time = current_time

    def draw(self, screen):
        if self.visible and self.alive:
            screen.blit(self.image, self.rect)

    def take_damage(self, damage):
        if self.visible and self.alive:
            self.health -= damage
            print(f"Boss health: {self.health}")

    def shooting_pattern(self):
        amount = 25  # Cantidad de balas en círculo
        origin_x = self.rect.centerx
        origin_y = self.rect.bottom - 100

        for i in range(amount):
            angle = math.radians(i * (360 / amount))
            direction = pygame.Vector2(math.cos(angle), math.sin(angle))
            bullet = BossBullet(origin_x, origin_y, direction, speed=4, settings=self.settings)
            self.bullet_group.add(bullet)

class BossBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, settings):
        super().__init__()
        self.image = pygame.Surface((12, 12))
        pygame.draw.circle(self.image, (255, 0, 0), (6, 6), 6)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction.normalize()
        self.speed = speed
        self.settings = settings

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        # Eliminar si sale de la pantalla
        if (
            self.rect.top > self.settings.screen_height or
            self.rect.bottom < 0 or
            self.rect.left < 0 or
            self.rect.right > self.settings.screen_width
        ):
            self.kill()

    
    