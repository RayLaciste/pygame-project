import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("main.py/data/assets/sword.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 140
        self.rect.y = 700
        
    def move(self):

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_q]:
            self.rect.x = 20
        if pressed_keys[pygame.K_w]:
            self.rect.x = 140
        if pressed_keys[pygame.K_e]:
            self.rect.x = 240

    def reset(self):
        self.rect.x = 140

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
