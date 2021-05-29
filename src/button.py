import pygame
from constants.colors import BUTTON_COLOR,BUTTON_TEXT_COLOR
from constants.window import BUTTON_HEIGHT,BUTTON_WIDTH

class Button:
    def __init__(self,x,y,text=''):
        self._x = x
        self._y = y
        self._text = text


    def is_mouse_over(self,mouse_position):
        is_mouse_inside_x = self._x < mouse_position[0] < self._x + BUTTON_WIDTH
        is_mouse_inside_y = self._y < mouse_position[1] < self._y + BUTTON_HEIGHT
        return is_mouse_inside_x and is_mouse_inside_y

    def draw(self, window):
        pygame.draw.rect(window, BUTTON_COLOR, (self._x, self._y, BUTTON_WIDTH, BUTTON_HEIGHT), 0)
        if self._text != '':
            font = pygame.font.SysFont('Arial', 25)
            text = font.render(self._text, True, BUTTON_TEXT_COLOR)
            window.blit(text, (self._x + (BUTTON_WIDTH// 2 - text.get_width() // 2),self._y + (BUTTON_HEIGHT // 2 - text.get_height() // 2)))