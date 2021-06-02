import pygame
from src.field import Field,Field_states,Players_type

class Board:
    def __init__(self,x_start,y_start,window,player_type):
        self._fields = [[Field(x_start+j*40,y_start+i*40,window,player_type) for j in range(10)]for i in range(10)]

    def draw_ship(self,position):
        for row in self._fields:
            for e in row:
                if e.is_mouse_over(position):
                    e.draw_ship_segment()