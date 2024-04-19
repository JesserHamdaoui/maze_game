import pygame
from os.path import join
from game.utilities.Object import Object

class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = self.get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def get_block(self, size):
        path = join("assets", "images", "objects", "ground", "Ground.png")
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(96, 0, size, size)
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale2x(surface)
#BLOCK2   
class Block2(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = self.get_second_block(size)  # Removed "Terrain.png" argument
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
    
    def get_second_block(self, size):
        path = join("assets", "images", "objects", "ground", "Ground.png")
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(96,64, size, size)  #ki khdit (0,0) khdhe awel block aamlt (96 besh nemsi aal limin baad adjust the numer besh yji el block bethabet)
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale2x(surface)

#Block3
class Block3(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = self.get_third_block(size)  
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
    
    def get_third_block(self, size):
        path = join("assets", "images", "objects", "ground", "Ground.png")
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(96,128, size, size)  
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale2x(surface)
