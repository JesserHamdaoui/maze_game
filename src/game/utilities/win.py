import pygame
import sys
from game.utilities.constants import WHITE, LIGHT_BLUE, font
from config.settings import WIDTH, HEIGHT
from game.scenes.menu import main_menu

def win_animation(window, clock, FPS):
    # You can create any animation or message you want to display when the player wins
    win_text = font.render("Congratulations! You've completed all levels!", True, WHITE)
    # Position the text at the center of the screen
    win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    # Display the text on the screen
    window.blit(win_text, win_rect)
    pygame.display.update()
    # Add a return button
    return_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
    pygame.draw.rect(window, LIGHT_BLUE, return_button)
    return_text = font.render("Game over", True, WHITE)
    window.blit(return_text, (return_button.x + 20, return_button.y + 10))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.collidepoint(event.pos):
                    return main_menu()  # Return to the main menu

        clock.tick(FPS)