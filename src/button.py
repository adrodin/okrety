import pygame
from constants.colors import BUTTON_COLOR,BUTTON_TEXT_COLOR


class Button:
    def __init__(self,x,y,width,height,color=BUTTON_COLOR,text=''):
        self._x = x
        self._y = y
        self._text = text
        self._width = width
        self._height = height
        self._color = color


    def is_mouse_over(self,mouse_position):
        is_mouse_inside_x = self._x < mouse_position[0] < self._x + self._width
        is_mouse_inside_y = self._y < mouse_position[1] < self._y + self._height
        return is_mouse_inside_x and is_mouse_inside_y

    def draw(self, window):
        pygame.draw.rect(window, self._color, (self._x, self._y, self._width, self._height), 0)
        if self._text != '':
            font = pygame.font.SysFont('Arial', 25)
            text = font.render(self._text, True, BUTTON_TEXT_COLOR)
            window.blit(text, (self._x + (self._width// 2 - text.get_width() // 2),self._y + (self._height // 2 - text.get_height() // 2)))


    def change_color(self,color,window):
        self._color = color
        self.draw(window)