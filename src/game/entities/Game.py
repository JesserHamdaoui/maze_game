import pygame
from game.utilities.constants import *
from game.entities.Player import Player
from game.entities.Block import Block
from game.entities.Coin import Coin
from game.entities.Checkpoint import Checkpoint
from game.entities.Enemy import Enemy
from game.entities.Fire import Fire
from game.user_interface.Healthbar import HealthBar
from game.user_interface.CoinCounter import CoinCounter
from game.user_interface.LevelIndicator import LevelIndicator
from game.user_interface.Background import Background
from config.settings import WIDTH, HEIGHT


class Game:
    def __init__(self, window, main_character):
        self.level = 0
        self.clock = pygame.time.Clock()
        self.background = Background("Blue.png")
        self.coins = pygame.sprite.Group()  # Group for coins
        self.block_size = 96
        self.maze_width = WIDTH // self.block_size
        self.maze_height = HEIGHT // self.block_size
        self.mazes = [
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 4, 0, 0, 0, 0, 1, 1, 1, 0, 2, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
                [1, 0, 0, 2, 0, 1, 2, 1, 1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [1, 2, 1, 0, 0, 1, 0, 2, 0, 0, 1, 3, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ],
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
                [1, 0, 0, 2, 0, 1, 2, 1, 1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
                [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [1, 2, 1, 0, 0, 1, 0, 2, 0, 0, 1, 3, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ],
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
                [1, 0, 0, 2, 0, 1, 2, 1, 1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
                [1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [1, 2, 1, 0, 0, 1, 0, 2, 0, 0, 1, 3, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]
        ]
        self.player = Player(100, 100, 50, 50, window, main_character)
        self.enemies_group = pygame.sprite.Group()
        self.fire = Fire(100, HEIGHT - self.block_size - 64, 16, 32)
        self.fire.on()
        self.objects = []
        self.offset_x = 0
        self.scroll_area_width = 200
        self.load_level()
        self.healthbar = HealthBar(20, 20, 200, 30, 100)
        self.coin_counter = CoinCounter(WIDTH - self.block_size * 2, 0, self.block_size)
        self.level_indicator = LevelIndicator(WIDTH - 100, HEIGHT - 30, self.level + 1)
        self.load_overlays(window)


    def load_level(self):
        self.objects.clear()
        for i in range(len(self.mazes[self.level])):
            for j in range(len(self.mazes[self.level][0])):
                if self.mazes[self.level][i][j] == 1:
                    self.objects.append(Block(j * self.block_size, i * self.block_size, self.block_size))
                elif self.mazes[self.level][i][j] == 2:
                    self.objects.append(Coin(j * self.block_size, i * self.block_size, self.block_size))
                elif self.mazes[self.level][i][j] == 3:
                    self.objects.append(Checkpoint(j * self.block_size - 32, i * self.block_size - 32, 64, 64))
                elif self.mazes[self.level][i][j] == 4:
                    blob = Enemy(j * self.block_size, i * self.block_size + 290)
                    self.enemies_group.add(blob)
        self.objects.append(self.fire)
        

    def load_overlays(self, window):
        self.healthbar.draw(window)
        self.coin_counter.draw(window)
        self.level_indicator.draw(window)

    def next_level(self):
        if self.level + 1 < len(self.mazes):
            self.level += 1
            self.level_indicator.update_level(self.level + 1)
            self.objects.clear()
            self.enemies_group.empty()
            self.player.rect.x = 100  # Reset player's x position
            self.player.rect.y = 100  # Reset player's y position
            self.offset_x = 0
            self.load_level()
        else:
            print("You've completed all levels!")

    def draw(self, window):    
        window.fill(BLACK)
        # Draw background tiles
        self.background.draw(window)
        # Draw objects (blocks, fire, etc.)
        for obj in self.objects:
            obj.draw(window, self.offset_x)

        self.player.draw(window, self.offset_x)
        # Draw the player

        for enemy in self.enemies_group:
            enemy.draw(window, self.offset_x)

        self.load_overlays(window)

        pygame.display.update()
