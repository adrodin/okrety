import pygame
import random
from enum import Enum
from src.field import Field,Field_states,Players_type

class Board:
    def __init__(self,x_start,y_start,window,player_type):
        self._x_start = x_start
        self._y_start = y_start
        self._state = Board_state.PREPARE
        self._player_type = player_type
        self._window = window
        if self._player_type == Players_type.PLAYER:
            self._can_interact = True
        else:
            self._can_interact = False
        self._fields = [[Field(x_start+j*40,y_start+i*40,window,player_type) for j in range(10)]for i in range(10)]
        self._ships = []
    def get_ships(self):
        return self._ships
    def draw_ship(self,position):
        if self._state == Board_state.PREPARE and self._player_type == Players_type.PLAYER:
            for row in self._fields:
                for e in row:
                    if e.is_mouse_over(position):
                        e.draw_ship_segment()

    def check_ships_position(self):

        i_was_here = [ ['no' for _ in range(10) ] for i in range(10)]
        ships_pattern = {
            4 : 1,
            3 : 2,
            2 : 3,
            1 : 4
        }
        for i in range(10):
            for j in range(10):
                if i_was_here[i][j] == 'no':
                    i_was_here[i][j] = 'yes'
                    if self._fields[i][j].get_field_state() == Field_states.SHIP:
                        self._ships.append((i,j))
                        ship_len = 1
                        row = False
                        #statek w rzedzie
                        for k in range(1,5):
                            if j+k < 10:
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

    def automatic_ships_generator(self):


        self._fields = [[Field(self._x_start + j * 40, self._y_start + i * 40, self._window, self._player_type) for j in range(10)] for i in range(10)]
        self._ships = []
        #---4x1
        x = random.randrange(7)
        y = random.randrange(7)
        z = random.randrange(7)
        self.add_ship(x,y,z,4)
        #3x2
        for _ in range(2):
            success = False
            while not success:
                x = random.randrange(8)
                y = random.randrange(8)
                z = random.randrange(2)
                success = self.can_add_ship(x,y,z,3)
                if success:
                     self.add_ship(x,y,z,3)
        #2x3
        for _ in range(3):
            success = False
            while not success:
                x = random.randrange(9)
                y = random.randrange(9)
                z = random.randrange(2)
                success = self.can_add_ship(x,y,z,2)
                if success:
                    self.add_ship(x,y,z,2)
        #1x4
        for _ in range(4):
            success = False
            while not success:
                x = random.randrange(10)
                y = random.randrange(10)
                z = random.randrange(2)
                success = self.can_add_ship(x, y, z, 1)
                if success:
                    self.add_ship(x, y, z, 1)
        self.check_ships_position()
        print(len(self._ships))
        return True

    def can_add_ship(self,x,y,z,size):
        if z == 0:
            for i in range(-1, size+1):
                if 0 <= x + i < 10:
                    if self._fields[x + i][y].get_field_state() == Field_states.SHIP:
                        return False
                    if y+1 < 10:
                        if self._fields[x + i ][y+1].get_field_state() == Field_states.SHIP:
                            return False
                    if y - 1 >= 0:
                        if self._fields[x + i ][y-1].get_field_state() == Field_states.SHIP:
                            return False

        else:
            for i in range(-1, size+1):
                if 0 <= y + i < 10:
                    if self._fields[x][y + i].get_field_state() == Field_states.SHIP:
                        return False
                    if x+1< 10:
                        if self._fields[x+1][y + i ].get_field_state() == Field_states.SHIP:
                            return False
                    if x -1 >= 0:
                        if self._fields[x-1][y + i ].get_field_state() == Field_states.SHIP:
                            return False
        return True

    def add_ship(self,x,y,z,size):
        if z == 0:
            for i in range(size):
                self._fields[x + i][y].draw_ship_segment()
        else:
            for i in range(size):
                self._fields[x][y + i].draw_ship_segment()

    def shot(self,x,y):
        response = self._fields[x][y].hit()
        if response == 1:
            self._ships.remove((x,y))
        return response


class Board_state(Enum):
    PREPARE = 0
    BATTLE = 1