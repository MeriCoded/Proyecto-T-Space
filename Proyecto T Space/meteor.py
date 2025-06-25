import pygame
from random import randint, uniform

class Meteor(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = None
        self.original_image = None
        self.rect = None
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.rotation = 0
        self.speed = 200
        self.health = 0
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000

    def update(self, delta_time):
        self.rect.center += self.direction * self.speed * delta_time
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

        self.rotation += 100 * delta_time
        self.image = pygame.transform.rotozoom(self.original_image, self.rotation, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def break_apart(self, all_groups):
        pass

    def get_points(self):
        return 0

class MeteorM1(Meteor):
    def __init__(self, pos, groups):
        super().__init__(pos, groups)
        self.original_image = pygame.image.load("Assets/Meteoritos/Meteorito1.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (60, 60))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.health = 0

    def get_points(self):
        return 10

class MeteorM2(Meteor):
    def __init__(self, pos, groups):
        super().__init__(pos, groups)
        self.original_image = pygame.image.load("Assets/Meteoritos/Meteorito2.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (65, 65))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.health = 20

    def get_points(self):
        return 30

class MeteorM3(Meteor):
    def __init__(self, pos, groups):
        super().__init__(pos, groups)
        self.original_image = pygame.image.load("Assets/Meteoritos/Meteorito3.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (80, 80))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.health = 30

    def get_points(self):
        return 60

class MeteorM4(Meteor):
    def __init__(self, pos, groups):
        super().__init__(pos, groups)
        self.original_image = pygame.image.load("Assets/Meteoritos/Meteorito4.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (80, 80))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.health = 50

    def break_apart(self, all_groups):
        baby1 = MeteorM1(self.rect.center, all_groups)
        baby2 = MeteorM1(self.rect.center, all_groups)
        baby1.direction = pygame.Vector2(uniform(-1, 0), 1).normalize()
        baby2.direction = pygame.Vector2(uniform(0, 1), 1).normalize()
        baby1.rotation = randint(0, 360)
        baby2.rotation = randint(0, 360)
    def get_points(self):
        return 80

class MeteorM5(Meteor):
    def __init__(self, pos, groups):
        super().__init__(pos, groups)
        self.original_image = pygame.image.load("Assets/Meteoritos/Meteorito3.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (100, 100))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.health = 100

    def break_apart(self, all_groups):
        baby1 = MeteorM1(self.rect.center, all_groups)
        baby2 = MeteorM1(self.rect.center, all_groups)
        baby3 = MeteorM1(self.rect.center, all_groups)
        baby1.direction = pygame.Vector2(uniform(-1, -0.5), 1).normalize()
        baby2.direction = pygame.Vector2(uniform(-0.5, 0.5), 1).normalize()
        baby3.direction = pygame.Vector2(uniform(0.5, 1), 1).normalize()
        baby1.rotation = randint(0, 360)
        baby2.rotation = randint(0, 360)
        baby3.rotation = randint(0, 360)
    def get_points(self):
        return 100

def create_meteor(tipo, pos, groups):
    if tipo == "M1":
        return MeteorM1(pos, groups)
    elif tipo == "M2":
        return MeteorM2(pos, groups)
    elif tipo == "M3":
        return MeteorM3(pos, groups)
    elif tipo == "M4":
        return MeteorM4(pos, groups)
    elif tipo == "M5": 
        return MeteorM5(pos, groups)
