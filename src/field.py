from src.button import Button
from constants.colors import SEA_COLOR
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



class Field_states(Enum):
    EMPTY = 0
    SHIP = 1
    HIT_SHIP = 2
    HIT_EMPTY = 3

class Players_type(Enum):
    PLAYER = 0
    BOT = 1