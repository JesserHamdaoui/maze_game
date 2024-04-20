import pygame
import os
import json
from game.utilities.shop import shop_items
from game.utilities.constants import *
from config.settings import WIDTH, HEIGHT
from game.scenes.main import main
from game.user_interface.CoinCounter import CoinCounter
from game.user_interface.buttons import ReturnButton

def shop_menu(window, clock):
    return_button = ReturnButton(WIDTH - 200, HEIGHT - 100, 200, 50, LIGHT_BLUE)
    with open('data\game.json', 'r') as file:
        data = json.load(file)
        coin_counter = CoinCounter(WIDTH - 96 * 2, 0, 96, data['coins'])
    
    while True:
        dt = clock.tick(60) / 1000.0  # Calculate delta time in seconds
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEMOTION:
                return_button.hover(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.is_over(event.pos):
                    return
                for item in shop_items:
                    if item.rect.collidepoint(event.pos):
                        with open('data\game.json', 'r+') as file:
                            if data['coins'] < item.price:
                                print("Not enough coins")
                                continue
                            data = json.load(file)
                            data['coins'] -= item.price
                            if item.name not in data['characters']:
                                data['characters'].append(item.name)
                            data['selected_character'] = item.name
                            file.seek(0)
                            json.dump(data, file, indent=4)
                            file.truncate()
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
            item.update()  # Pass dt to the update method
            item.draw(window, x, y)
            x += 300

        # Draw return button
        return_button.draw(window)
        
        coin_counter.loop()
        coin_counter.draw(window)
        pygame.display.update()
