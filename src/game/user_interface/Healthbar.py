import pygame
from game.utilities.constants import RED, GREEN

class HealthBar():
    def __init__(self,x,y,w,h,max_hp):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.hp=max_hp
        self.max_hp=max_hp
    def draw(self,surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface,RED,(self.x ,self.y ,self.w ,self.h))
        pygame.draw.rect(surface,GREEN ,(self.x ,self.y, self.w * ratio, self.h))
