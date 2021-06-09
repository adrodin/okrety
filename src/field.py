from src.button import Button
from constants.colors import SEA_COLOR,SHIP_COLOR,HIT_SHIP_COLOR,HIT_SEA_COLOR
from enum import Enum

class Field(Button):
    def __init__(self, x, y,window,player_type):
        """
        Inicjalizacja pola
        :param x: pozycja x pola
        :param y: pozycja y pola
        :param window: okno w, którym pole będzie wyświetlane
        :param player_type: typ gracza (PLAYER lub BOT)
        """
        self._window = window
        self._field_state = FieldStates.EMPTY
        self._can_shoot = True
        self._player_type = player_type
        super().__init__(x,y,width=30,height=30,color=SEA_COLOR)
        super().draw(self._window)

    def get_field_state(self):
        """
        Zwrócenie statusu pola
        :return: zwraca jeden z 4 możliwych (FieldStates) stanów pola
        """
        return self._field_state

    def hit(self):
        """
        Strzał w pole
        :return: zwraca 0 jeśli zostało strzelone w pole, 1 jeśli w statek, -1 w pozostałych przypadkach
        """
        if self._can_shoot is True:
            if self._field_state == FieldStates.EMPTY:
                self._can_shoot = False
                super().change_color(HIT_SEA_COLOR,self._window)
                self._field_state = FieldStates.HIT_EMPTY
                return 0
            if self._field_state == FieldStates.SHIP:
                self._can_shoot = False
                super().change_color(HIT_SHIP_COLOR,self._window)
                self._field_state = FieldStates.HIT_SHIP
                return 1
        return -1

    def draw_ship_segment(self):
        """
        Rysowanie segmentu statku
        :return: 1 gdy nastąpiła zamiana EMPTY->SHIP, -1 gdy SHIP->empty
        """
        if self._field_state == FieldStates.EMPTY:
            self._field_state = FieldStates.SHIP
            if self._player_type ==PlayersType.PLAYER:
                super().change_color(SHIP_COLOR,self._window)
            return 1
        else:
            self._field_state = FieldStates.EMPTY
            super().change_color(SEA_COLOR,self._window)
            return -1



class FieldStates(Enum):
    EMPTY = 0
    SHIP = 1
    HIT_SHIP = 2
    HIT_EMPTY = 3

class PlayersType(Enum):
    PLAYER = 0
    BOT = 1