import pygame
from game.utilities.Object import Object
from game.utilities.sprite import load_sprite_sheets

class Coin(Object):
    ANIMATION_DELAY = 3
    def __init__(self, x, y, size):
        super().__init__(x + 32, y + 32, size, size, "coin")
        self.coin = load_sprite_sheets(["objects", "coin"], 16, 16)
        self.image = self.coin["coin"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "coin"

    def loop(self):
        sprites = self.coin[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
