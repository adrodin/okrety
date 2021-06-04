import pygame
from enum import Enum
from src.field import Field,Field_states,Players_type

class Board:
    def __init__(self,x_start,y_start,window,player_type):
        self._state = Board_state.PREPARE
        self._player_type = player_type
        self._window = window
        if self._player_type == Players_type.PLAYER:
            self._can_interact = True
        else:
            self._can_interact = False
        self._fields = [[Field(x_start+j*40,y_start+i*40,window,player_type) for j in range(10)]for i in range(10)]
        self._ships = []

    def draw_ship(self,position):
        if self._state == Board_state.PREPARE and self._player_type == Players_type.PLAYER:
            for row in self._fields:
                for e in row:
                    if e.is_mouse_over(position):
                        e.draw_ship_segment()

    def check_ships_position(self):

        i_was_here = [ ['no' for j in range(10) ] for i in range(10)]
        ships_pattern = {
            4 : 1,
            3 : 2,
            2 : 3,
            1 : 4
        }
        for i in range(10):
            for j in range(10):
                print(f'xd {i} {j}')
                if i_was_here[i][j] == 'no':
                    i_was_here[i][j] = 'yes'
                    if self._fields[i][j].get_field_state() == Field_states.SHIP:
                        self._ships.append((i,j))
                        ship_len = 1
                        row = False
                        #statek w rzedzie
                        for k in range(1,5):
                            if j+k < 10:
                                print(k)
                                if i_was_here[i][j+k] == 'yes' and self._fields[i][j+k].get_field_state() == Field_states.SHIP:
                                    return False
                                if self._fields[i][j+k].get_field_state() == Field_states.SHIP and j != 9:
                                    row = True
                                    i_was_here[i][j+k] = 'yes'
                                    self._ships.append((i,j+k))
                                    ship_len += 1
                                else:
                                    break
                        #statki w kolumnie
                        for k in range(1,5):
                            if i + k < 10:
                                if i_was_here[i+k][j] == 'yes' and self._fields[i+k][j].get_field_state() == Field_states.SHIP:
                                    return False
                                if self._fields[i+k][j].get_field_state() == Field_states.SHIP and i != 9:
                                    if row is True:
                                        return False
                                    i_was_here[i+k][j] = 'yes'
                                    self._ships.append((i+k,j))
                                    ship_len += 1
                                else:
                                    break

                        if ship_len == 5:
                            return False
                        ships_pattern[ship_len] -= 1
                        #nie stykanie się nastepnych
                        for k in range(-1,ship_len+1):
                            if row is True:
                                if k+j != -1 and k+j != 10 and i != 9:
                                    if self._fields[i+1][j+k].get_field_state() == Field_states.SHIP:
                                        return False
                                    else:
                                        i_was_here[i+1][j+k] = 'yes'
                            else:
                                if k+i != -1 and k+i != 10 and j != 9:
                                    if self._fields[i+k][j+1].get_field_state() == Field_states.SHIP:
                                        return False
                                    else:
                                        i_was_here[i+k][j+1] = 'yes'
                                if k+i != -1 and k+i != 10 and j != 0:
                                    if self._fields[i+k][j-1].get_field_state() == Field_states.SHIP:
                                        return False
                                    else:
                                        i_was_here[i+k][j-1] = 'yes'

        if ships_pattern[1] != 0:
            return False
        if ships_pattern[2] != 0:
            return False
        if ships_pattern[3] != 0:
            return False
        if ships_pattern[4] != 0:
            return False
        return True

    def check_win(self):
        return len(self._ships == 0)

class Board_state(Enum):
    PREPARE = 0
    BATTLE = 1