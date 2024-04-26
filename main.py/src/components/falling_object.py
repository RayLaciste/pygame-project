import pygame
import random


class FallingObject(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("main.py/data/assets/shuriken.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = random.uniform(-250, -1000)
        self.orig_y = self.rect.y
        self.speed = random.uniform(7, 13)

    def loop(self):
        self.rect.y = -50
        self.speed = random.uniform(6, 12)

    def reset(self):
        self.rect.y = self.orig_y

    def update(self):
        self.rect.move_ip(0, self.speed)