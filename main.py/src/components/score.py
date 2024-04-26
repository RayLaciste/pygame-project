import pygame

class Scoreboard:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font('freesansbold.ttf', 48)
        self.score = 0
        self.text_surface = self.font.render(str(self.score), True, 'Black')
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (360 / 2, 760)

    def increment_score(self):
        self.score += 1
        self.update_text()

    def reset_score(self):
        self.score = 0
        self.update_text()

    def update_text(self):
        self.text_surface = self.font.render(str(self.score), True, 'Black')

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)
