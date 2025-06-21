import pygame
from settings import Settings

class Meteor(pygame.sprite.Sprite):
    def __init__(self, game, x, y, tipo="M1"):
        super().__init__()
        self.game = game
        self.tipo = "M1"

        if tipo == "M1":
            size = (70, 60)
            img_range = range(1, 3)
        elif tipo == "M2":
            size = (90, 80)
            img_range = range(3, 5)
        elif tipo == "M3":
            size = (110, 100)
            img_range = range(5, 7)
        else:
            size = (80, 70)
            img_range = range(2, 4)

        self.images = []
        for i in img_range:
            meteor_img = pygame.image.load(f"Proyecto T Space/assets/Meteoritos/Meteorito{i}.png").convert_alpha()
            meteor_img = pygame.transform.scale(meteor_img, size)
            self.images.append(meteor_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
    
    def break_apart(self):
        # Solo el meteorito grande ("M4") se divide
        if self.tipo == "M4":
            # Crea dos meteoritos pequeños en la posición del grande
            for dx in [-20, 20]:
                new_meteor = Meteor(self.game, self.rect.x + dx, self.rect.y, tipo="M1")
                self.game.meteors_pequenos.add(new_meteor)

