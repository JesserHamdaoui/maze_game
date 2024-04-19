import pygame
import os
from config.settings import WIDTH, HEIGHT, FPS
from game.entities.Game import Game
from game.utilities.sound import jump_fx, game_over_fx
from game.utilities.movement import handle_move

def main(window, clock = pygame.time.Clock(), main_character = "VirtualGuy"):
    game = Game(window, clock, FPS, main_character)
    game.load_level()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.player.jump_count < 2:
                    game.player.jump()
                    jump_fx.play()  # Play jump sound when the player jumps


        game.player.loop(FPS)
        game.coin_counter.loop()
        game.fire.loop()

        for obj in game.objects:
            if obj.name == "checkpoint":
                obj.loop()
            elif obj.name == "coin":
                obj.loop()

        for enemy in game.enemies_group:
            enemy.loop()
            enemy.update()
        
        handle_move(game)
        enemy_hit = pygame.sprite.spritecollide(game.player, game.enemies_group, False)
        if enemy_hit:
            game.player.make_hit()


        # Update health bar based on player's hit status
        if game.player.hit:
           game.healthbar.hp -= 0.3 # Decrease health by 10 (adjust as needed)
        # Check if player's health is empty or critical

        
        if game.healthbar.hp <= 0:
            game.player.alive = False
            game.player.draw(window, game.offset_x)
            # draw_text('GAME OVER!', font, WHITE, (WIDTH // 2) - 200, HEIGHT // 2)
            game_over_fx.play()
            #pygame.mixer.music.stop()
            restart_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 100, 200, 50)
                        

            def draw_restart_button():
                restart_img = pygame.image.load(os.path.join('/Users/gastonguelmami/Desktop/maze_game-main/assets/images/user-interface/Menu/Buttons/Restart.png'))
                window.blit(restart_img, (WIDTH//2 - restart_img.get_width()//2, HEIGHT//2 + 100))
            draw_restart_button()  # Display the restart button
            pygame.display.update()  # Update the display
            # Wait for a mouse click on the restart button
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            main(window)  # Restart the game
                            return
        else:
            game.healthbar.draw(window)
            game.draw(window)
        



        if ((game.player.rect.right - game.offset_x >= WIDTH - game.scroll_area_width) and game.player.x_vel > 0) or (
                (game.player.rect.left - game.offset_x <= game.scroll_area_width) and game.player.x_vel < 0):
            game.offset_x += game.player.x_vel

    pygame.quit()
    quit()
