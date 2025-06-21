import pygame
from random import randint, uniform
#from main import Window, delta_time

#Diccionario global para las imágenes
meteor_images = {}

def load_meteor_images():
    global meteor_images
    base_image1 = pygame.image.load("Assets/Meteoritos/Meteorito1_v2.png").convert_alpha()
    base_image2 = pygame.image.load("Assets/Meteoritos/Meteorito2_v2.png").convert_alpha()
    base_image3 = pygame.image.load("Assets/Meteoritos/Meteorito3_v2.png").convert_alpha()
    base_image4 = pygame.image.load("Assets/Meteoritos/Meteorito4_v3.png").convert_alpha()

    meteor_images = {
        "M1": pygame.transform.scale(base_image1, (60, 60)),
        "M2": pygame.transform.scale(base_image2, (65, 65)),
        "M3": pygame.transform.scale(base_image3, (75, 75)),
        "M4": pygame.transform.scale(base_image4, (80, 80))
    }

class Meteor(pygame.sprite.Sprite):
    def __init__(self, tipo, pos, groups):
        super().__init__(groups)
        self.original_image = meteor_images[tipo]
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        #self.mask = pygame.mask.from_surface(self.image) - No es necesario escribirlo, lo dejo para estudiar
        self.rotation = 0

        #Velocidad según tamaño
        speed_ranges = {
            "M1": (500, 600),
            "M2": (400, 500),
            "M3": (300, 400),
            "M4": (200, 300)
        }
        self.speed = randint(*speed_ranges[tipo])

    def update(self, delta_time):
        self.rect.center += self.direction * self.speed * delta_time
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()
        
        # Para hacer que los meteoritos roten continuamente
        self.rotation += 100 * delta_time
        self.image = pygame.transform.rotozoom(self.original_image, self.rotation, 1)
        self.rect = self.image.get_rect(center = self.rect.center)
            
    