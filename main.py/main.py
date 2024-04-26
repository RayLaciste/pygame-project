import pygame
import time

from src.components.falling_object import FallingObject
from src.components.player import Player
from src.components.score import Scoreboard
from src.components.sound_manager import SoundManager

WIN_WIDTH = 360
PADDING = 40
OBJ_LEN = 40

scoreboard = Scoreboard()

P1 = Player()
F1 = FallingObject(PADDING)
F2 = FallingObject((PADDING * 2) + (OBJ_LEN * 2))
F3 = FallingObject((PADDING * 3) + (OBJ_LEN * 4))

# Sprite groups
falling_objects = pygame.sprite.Group()
falling_objects.add(F1)
falling_objects.add(F2)
falling_objects.add(F3)
all_sprites = pygame.sprite.Group()
all_sprites.add(F1)
all_sprites.add(F2)
all_sprites.add(F3)
all_sprites.add(P1)


def start_menu(screen, bg, high_score):
    # Display start message
    title = (pygame.font.Font('freesansbold.ttf', 32).
             render("Shuriken Defense!", True, 'Black'))
    title_rect = title.get_rect(center=(360 / 2, 300))

    start_text = (pygame.font.Font('freesansbold.ttf', 24).
                  render("Press any key to start", True, 'Red'))
    start_text_rect = start_text.get_rect(center=(360 / 2, 400))

    high_score_text = (pygame.font.Font('freesansbold.ttf', 24).
                       render("High Score: " + str(high_score), True, 'Black'))
    high_score_text_rect = high_score_text.get_rect(center=(360 / 2, 450))

    instructions = (pygame.font.Font('freesansbold.ttf', 24).
                    render("move with Q W E", True, 'Black'))
    instructions_rect = instructions.get_rect(center=(360 / 2, 500))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                time.sleep(0.5)
                return

        # Draw start message
        screen.fill('white')
        screen.blit(bg, (0, 0))
        screen.blit(title, title_rect)
        screen.blit(start_text, start_text_rect)
        screen.blit(high_score_text, high_score_text_rect)
        screen.blit(instructions, instructions_rect)

        pygame.display.flip()


def in_game(screen, clock, bg):
    sound_manager = SoundManager()
    sound_manager.play_bg_music()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True

        clock.tick(60)

        # Update background
        screen.fill('white')
        screen.blit(bg, (0, 0))

        # draw sprite group
        falling_objects.draw(screen)
        P1.draw(screen)

        # update sprite group
        falling_objects.update()
        P1.move()

        # Collision detection
        for falling_object in falling_objects:
            if P1.rect.colliderect(falling_object.rect):
                scoreboard.increment_score()
                sound_manager.play_block_sound()
                falling_object.loop()
            if falling_object.rect.top > 800:
                sound_manager.play_hit_sound()
                F1.reset()
                F2.reset()
                F3.reset()
                time.sleep(0.5)
                return True

        scoreboard.draw(screen)

        pygame.display.flip()

    return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((360, 800))
    clock = pygame.time.Clock()
    bg = pygame.image.load("main.py/data/assets/bg.png")
    high_score = 0

    while True:
        start_menu(screen, bg, high_score)
        scoreboard.reset_score()
        game_over = in_game(screen, clock, bg)
        if game_over:
            time.sleep(0.5)
            print(str(scoreboard.score))
            if scoreboard.score > high_score:
                high_score = scoreboard.score  # Update high score if current score is higher


main()
