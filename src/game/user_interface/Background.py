import pygame
from os.path import join
from config.settings import WIDTH, HEIGHT

class Background:
    def __init__(self, name):
        self.image = pygame.image.load(join("assets", "images", "user-interface", "Background", name))
        _, _, self.width, self.height = self.image.get_rect()
        self.tiles = []

        for i in range(WIDTH // self.width + 1):
            for j in range(HEIGHT // self.height + 1):
                pos = (i * self.width, j * self.height)
                self.tiles.append(pos)

    def draw(self, window):
        for pos in self.tiles:
            window.blit(self.image, pos)