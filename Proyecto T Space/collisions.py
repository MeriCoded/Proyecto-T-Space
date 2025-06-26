import pygame

def collisions():
    collision_sprite = pygame.sprite.spritecollide(player, meteor_sprites, True)
    
    if collision_sprite:
        print(collision_sprite[0])
        
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()