import pygame
from game.utilities.constants import LIGHT_BLUE, WHITE, font

class Button():
    def __init__(self, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text

    def draw(self, window, outline=None):
        if outline:
            pygame.draw.rect(window, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
    
    def hover(self, pos):
        if self.is_over(pos):
            self.color = LIGHT_BLUE
        else:
            self.color = WHITE


class ReturnButton(Button):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color, "Return")
