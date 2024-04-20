import pygame
from game.utilities.constants import PLAYER_VEL
from game.utilities.collision import collide, handle_vertical_collision
from game.utilities.sound import coin_fx, health_up_fx

def handle_move(game):
    keys = pygame.key.get_pressed()

    game.player.x_vel = 0
    collide_left = collide(game.player, game.objects, -PLAYER_VEL * 2)
    collide_right = collide(game.player, game.objects, PLAYER_VEL * 2)

    if keys[pygame.K_LEFT] and not collide_left:
        game.player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not collide_right:
        game.player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(game.player, game.objects, game.player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            game.player.make_hit()
        elif obj and obj.name == "coin":
            if obj in game.objects:
                coin_fx.play()
                game.coin_counter.increase_count()
                game.objects.remove(obj)
        elif obj and obj.name == "heart":
            if obj in game.objects:
                game.healthbar.increase_hp(30)
                game.objects.remove(obj)
                health_up_fx.play()
        elif obj and obj.name == "checkpoint":
            if obj in game.objects:
                game.objects.remove(obj)
                game.next_level()
