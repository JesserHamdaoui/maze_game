import pygame
import sys
from config.settings import WIDTH, HEIGHT
from game.user_interface.buttons import ReturnButton
from game.utilities.constants import WHITE, LIGHT_BLUE, font


def game_over_animation(window, clock, FPS):
    # Create the game over text
    game_over_text = font.render("Game Over", True, WHITE)
    # Position the text at the center of the screen
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    # Display the text on the screen
    window.blit(game_over_text, game_over_rect)
    pygame.display.update()
    
    # Add a return button
    return_button = ReturnButton(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, WHITE)
    return_button.draw(window)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.is_over(event.pos):
                    return False  # Return to the main menu
        clock.tick(FPS)
