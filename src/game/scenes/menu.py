import pygame
import sys
import os
from config.settings import WIDTH, HEIGHT
from game.utilities.constants import LIGHT_BLUE, WHITE, font

def main_menu(window):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    print("play")
                    return "play"
                elif shop_button.collidepoint(event.pos):
                    return "shop"
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Display background image
        background_image = pygame.image.load(os.path.join("assets","images","user-interface","Menu","Background","background.jpg"))
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale the background image to match window dimensions
        window.blit(background_image, (0, 0))

        # Draw menu buttons
        play_button = pygame.Rect(WIDTH//2 - 100, 200, 200, 50)
        shop_button = pygame.Rect(WIDTH//2 - 100, 300, 200, 50)
        quit_button = pygame.Rect(WIDTH//2 - 100, 400, 200, 50)
        pygame.draw.rect(window, LIGHT_BLUE, play_button)
        pygame.draw.rect(window, LIGHT_BLUE, shop_button)
        pygame.draw.rect(window, LIGHT_BLUE, quit_button)

        # Draw button labels
        play_text = font.render("Play", True, WHITE)
        window.blit(play_text, (play_button.x + 50, play_button.y + 10))
        shop_text = font.render("Shop", True, WHITE)
        window.blit(shop_text, (shop_button.x + 50, shop_button.y + 10))
        quit_text = font.render("Quit", True, WHITE)
        window.blit(quit_text, (quit_button.x + 50, quit_button.y + 10))

        pygame.display.update()
