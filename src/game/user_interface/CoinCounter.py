import pygame
import json
from game.utilities.Object import Object
from game.utilities.sprite import load_sprite_sheets
from game.utilities.constants import WHITE

class CoinCounter(Object):
    ANIMATION_DELAY = 3
    def __init__(self, x, y, size, coin_count=0):
        super().__init__(x + 32, y + 32, size, size, "coin")
        self.x = x + 32
        self.y = y + 32
        self.coin = load_sprite_sheets(["objects", "coin"], 16, 16)
        self.image = self.coin["coin"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "coin"
        self.count = coin_count

    def increase_count(self, score=1):
        self.count += score
        # Update the coin count in the game.json file
        with open('/Users/gastonguelmami/Desktop/maze_game-main/data/game.json', 'r+') as file:
            data = json.load(file)
            data['coins'] += score
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

    def draw(self, win):
        win.blit(self.image, (self.rect.x , self.rect.y))
        score_surface = pygame.font.Font(None, 40).render(f"x {self.count}", True, WHITE)
        win.blit(score_surface, (self.x + 32, self.y + 4))
    
    def loop(self):
        sprites = self.coin[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
