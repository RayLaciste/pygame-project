import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.block_sfx = pygame.mixer.Sound('main.py/data/audio/block.wav')
        self.hit_sfx = pygame.mixer.Sound('main.py/data/audio/hit.wav')
        self.bg_music = pygame.mixer.music.load('main.py/data/audio/bg_music.wav')

    def play_block_sound(self):
        pygame.mixer.Sound.play(self.block_sfx)

    def play_hit_sound(self):
        pygame.mixer.Sound.play(self.hit_sfx)

    def play_bg_music(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

    def stop_bg_music(self):
        pygame.mixer.music.stop()

    def pause_bg_music(self):
        pygame.mixer.music.pause()

    def unpause_bg_music(self):
        pygame.mixer.music.unpause()