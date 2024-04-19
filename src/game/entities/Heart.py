# import pygame
# from game.utilities.Object import Object
# from game.utilities.sprite import load_sprite_sheets

# class Heart(Object):
#     ANIMATION_DELAY = 3

#     def __init__(self, x, y):
#         super().__init__(x + 32, y + 32, 16, 16, "heart")
#         self.heart = load_sprite_sheets("objects", "heart", 16, 16)
#         self.image = self.heart["heart"][0]
#         self.mask = pygame.mask.from_surface(self.image)
#         self.animation_count = 0
#         self.animation_name = "heart"

#     def loop(self):
#         sprites = self.heart[self.animation_name]
#         sprite_index = (self.animation_count //
#                         self.ANIMATION_DELAY) % len(sprites)
#         self.image = sprites[sprite_index]
#         self.animation_count += 1

#         self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
#         self.mask = pygame.mask.from_surface(self.image)

#         if self.animation_count // self.ANIMATION_DELAY > len(sprites):
#             self.animation_count = 0

#     def update(self):
#         pass  # Heart doesn't need any specific update behavior

#     def draw(self, win, offset_x):
#         win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
