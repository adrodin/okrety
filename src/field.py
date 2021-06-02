from src.button import Button
from constants.colors import SEA_COLOR,SHIP_COLOR,HIT_SHIP_COLOR,HIT_SEA_COLOR
from enum import Enum

class Field(Button):
    def __init__(self, x, y,window,player_type):
        self._window = window
        self._field_state = Field_states.EMPTY
        self._can_shoot = True
        self._player_type = player_type
        super().__init__(x,y,width=30,height=30,color=SEA_COLOR)
        super().draw(self._window)

    def get_field_state(self):
        return self._field_state

    def hit(self):
        if self._can_shoot is True:
            if self._field_state == Field_states.EMPTY:
                self._can_shoot = False
                super().change_color(HIT_SEA_COLOR,self._window)
                self._field_state = Field_states.HIT_EMPTY
                return 0
            if self._field_state == Field_states.SHIP:
                self._can_shoot = False
                super().change_color(HIT_SHIP_COLOR,self._window)
                self._field_state = Field_states.HIT_SHIP
                return 1
        return -1

    def draw_ship_segment(self):
        if self._field_state == Field_states.EMPTY:
            self._field_state = Field_states.SHIP
            if self._player_type ==Players_type.PLAYER:
                super().change_color(SHIP_COLOR,self._window)
        else:
            self._field_state = Field_states.EMPTY
            super().change_color(SEA_COLOR,self._window)



class Field_states(Enum):
    EMPTY = 0
    SHIP = 1
    HIT_SHIP = 2
    HIT_EMPTY = 3

class Players_type(Enum):
    PLAYER = 0
    BOT = 1