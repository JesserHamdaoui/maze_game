import pygame
import json
from game.utilities.constants import WHITE, font
from game.utilities.sprite import load_sprite_sheets

class ShopItem:
    ANIMATION_DELAY = 3

    def __init__(self, name, price, image_path):
        self.name = name
        self.price = price
        self.sprites = load_sprite_sheets(["characters", "player", name], 32, 32, True)
        self.sprite_width = 32
        self.sprite_height = 32
        self.current_frame = 0
        self.animation_frames = 4  # Number of frames in the animation
        self.animation_speed = 0.2  # Speed of animation (in seconds)
        self.animation_timer = 0
        self.scale_factor = 3
        self.rect = pygame.Rect(0, 0, self.sprite_width * 2, self.sprite_height * 2)
  

    def draw(self, window, x, y):
        self.rect.topleft = (x, y)
        window.blit(self.sprite, (self.rect.x, self.rect.y))

        text_name = font.render(self.name, True, WHITE)
        with open('data\game.json', 'r') as file:
            data = json.load(file)
            if self.name in data['characters']:
                self.price = 0
        if self.price == 0:
            text_price = font.render("Acquired!", True, WHITE)
            pygame.draw.rect(window, (0, 0, 255), (x, y, self.rect.width, self.rect.height), 2)
        else:
            text_price = font.render(f"${self.price}", True, WHITE)
        window.blit(text_name, (x + 10, y - 30))
        pygame.draw.rect(window, (0, 0, 0), (x, y + self.rect.height + 5, text_price.get_width() + 20, text_price.get_height()), 0)
        window.blit(text_price, (x + 10, y + self.rect.height + 5))
        

    def update(self):
        sprite_sheet_name =  "idle_right"
        sprites = self.sprites[sprite_sheet_name]
        sprite_index = (self.current_frame // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.current_frame += 1
