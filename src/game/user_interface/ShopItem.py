import pygame
from game.utilities.constants import WHITE, font

class ShopItem:
    def __init__(self, name, price, image_path):
        self.name = name
        self.price = price
        self.sprite_sheet = pygame.image.load("assets\images\\" + '\\'.join(image_path) + '\idle.png')
        self.sprite_width = 32
        self.sprite_height = 32
        self.current_frame = 0
        self.animation_frames = 4  # Number of frames in the animation
        self.animation_speed = 0.2  # Speed of animation (in seconds)
        self.animation_timer = 0
        self.scale_factor = 3
        self.rect = pygame.Rect(0, 0, self.sprite_width * 3, self.sprite_height * 3)

    def draw(self, window, x, y):
        self.rect.topleft = (x, y)
        window.blit(self.sprite_sheet, self.rect, (self.current_frame * self.sprite_width, 0, self.sprite_width, self.sprite_height))
        text_name = font.render(self.name, True, WHITE)
        text_price = font.render(f"${self.price}", True, WHITE)
        window.blit(text_name, (x + 10, y - 30))
        window.blit(text_price, (x + 10, y + self.rect.height + 5))

    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % self.animation_frames
