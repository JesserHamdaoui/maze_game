import pygame
from config.settings import WIDTH, HEIGHT, FPS
from game.entities.Game import Game
from game.utilities.sound import jump_fx, game_over_fx
from game.utilities.movement import handle_move
from game.user_interface.buttons import ReturnButton
from game.utilities.game_over import game_over_animation

def main(window, main_character="VirtualGuy"):
    clock = pygame.time.Clock()
    game = Game(window, main_character, FPS, clock)
    game.load_level()
    restart_button = ReturnButton(0, HEIGHT - 50, 200, 50, (0, 0, 0))

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.player.jump_count < 2:
                    game.player.jump()
                    jump_fx.play()

            elif event.type == pygame.MOUSEMOTION:
                restart_button.hover(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.is_over(event.pos):
                    run = False
                    break

        game.player.loop(FPS)
        game.coin_counter.loop()
        game.fire.loop()

        for obj in game.objects:
            if obj.name == "checkpoint" or obj.name == "coin":
                obj.loop()

        for enemy in game.enemies_group:
            enemy.loop()
            enemy.update()

        handle_move(game)
        enemy_hit = pygame.sprite.spritecollide(game.player, game.enemies_group, False)
        if enemy_hit:
            game.player.make_hit()

        if game.player.hit:
            game.healthbar.hp -= 0.3

        if game.healthbar.hp <= 0:
            game.player.alive = False
            game.player.draw(window, game.offset_x)
            game_over_fx.play()
            run = game_over_animation(window, clock, FPS)
            break
        
        else:
            game.draw(window, restart_button)

        if ((game.player.rect.right - game.offset_x >= WIDTH - game.scroll_area_width) and game.player.x_vel > 0) or (
                (game.player.rect.left - game.offset_x <= game.scroll_area_width) and game.player.x_vel < 0):
            game.offset_x += game.player.x_vel

    return
