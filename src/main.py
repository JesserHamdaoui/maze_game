import pygame
from config.settings import WIDTH, HEIGHT
from game.scenes.main import main
from game.scenes.shop import shop_menu
from game.scenes.menu import main_menu

pygame.init()

pygame.display.set_caption("Maze")

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.mixer.music.load('assets\sounds\\background\music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)

if __name__ == "__main__":
    while True:
        choice = main_menu(window)
        if choice == "play":
            main(window)
            main_menu(window)
        elif choice == "shop":
            if shop_menu(window, clock) == "menu":
                main_menu(window)