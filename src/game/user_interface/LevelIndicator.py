import pygame
from game.utilities.constants import WHITE, BLACK

class LevelIndicator():
    def __init__(self, x, y, level=1):
        self.x = x
        self.y = y
        self.level = level

    def update_level(self, level):
        self.level = level
    
    def draw(self, window):
        level_surface = pygame.font.Font(None, 40).render(f"Level {self.level}", True, WHITE)
        level_rect = level_surface.get_rect()
        level_rect.topleft = (self.x, self.y)
        pygame.draw.rect(window, BLACK, level_rect)
        window.blit(level_surface, (self.x, self.y))

