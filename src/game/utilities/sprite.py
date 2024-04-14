import pygame
from os import listdir
from os.path import isfile, join

def load_sprite_sheets(dirs, width, height, direction=False, window=pygame.display.set_mode((800, 600))):
    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
    
    print(pygame.display.Info())
    all_sprites = {}

    path = join("assets", "images", *dirs)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    for image in images:
        print("******", join(path, image))
        if image == ".DS_Store":
            continue
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha(window)
        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites