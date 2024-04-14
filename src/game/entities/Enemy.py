import pygame
from game.utilities.Object import Object
from game.utilities.sprite import load_sprite_sheets

class Enemy(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y):
        super().__init__(x, y - 32 - 96*2, 16, 16, "enemy")
        self.initial_x = x
        self.enemy = load_sprite_sheets(["characters", "enemies", "Blob"], 16, 16)
        for direction in self.enemy:
            sprites = self.enemy[direction]
            for i in range(len(sprites)):
                sprites[i] = pygame.transform.scale(sprites[i], (32, 32))
        self.image = self.enemy["right"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.x_vel = 1
        self.animation_name = "right"
        self.animation_count = 0

    def update(self):
        self.rect.x += self.x_vel
        if self.rect.x <= self.initial_x or self.rect.x >= self.initial_x + 96 - 24:
            self.x_vel *= -1
            if self.x_vel > 0:
                self.animation_name = "right"
            else:
                self.animation_name = "left"

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

    def loop(self):
        sprites = self.enemy[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
