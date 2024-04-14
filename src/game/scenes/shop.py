import pygame
import os
from game.utilities.shop import shop_items
from game.utilities.constants import *
from config.settings import WIDTH, HEIGHT
from game.scenes.main import main

def shop_menu(window, clock):
    return_button = pygame.Rect(WIDTH//2 - 100, HEIGHT - 100, 200, 50)
    
    while True:
        dt = clock.tick(60) / 1000.0  # Calculate delta time in seconds
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.collidepoint(event.pos):
                    return  # Return to the main menu
                for item in shop_items:
                    if item.rect.collidepoint(event.pos):
                        main(window, main_character=item.name)  # Call the main function with the name of the clicked character as a parameter

        # Clear the screen
        window.fill(BLACK)

        # Display background image
        background_image = pygame.image.load(os.path.join("assets","images","user-interface","Menu","Background","background.jpg"))
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale the background image to match window dimensions
        window.blit(background_image, (0, 0))

        # Update and draw shop items
        x, y = 50, 50
        for i, item in enumerate(shop_items):
            if i % 2 == 0 and i != 0:
                x = 50
                y += 250
            item.update(dt)  # Pass dt to the update method
            item.draw(window, x, y)
            x += 300

        # Draw return button
        pygame.draw.rect(window, LIGHT_BLUE, return_button)
        return_text = font.render("Return", True, WHITE)
        window.blit(return_text, (return_button.x + 50, return_button.y + 10))
        
        pygame.display.update()
