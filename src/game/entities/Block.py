import pygame
from os.path import join
from game.utilities.Object import Object

class Block(Object):
    def __init__(self, x, y, size, block_type=1):
        super().__init__(x, y, size, size)
        block = self.get_block(size, block_type)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def get_block(self, size, block_type):
        path = join("assets", "images", "objects", "ground", "Ground.png")
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(96, 64*(block_type - 1), size, size)
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale2x(surface)
