import pygame
import random
from enum import Enum
from src.field import Field,FieldStates,PlayersType
from constants.colors import SEA_COLOR

class Board:
    def __init__(self,x_start,y_start,window,player_type):
        """
        Inicjalizacja pojedynczej planszy
        """
        self._x_start = x_start
        self._y_start = y_start
        self._player_type = player_type
        self._window = window
        self._fields = [[Field(x_start+j*40,y_start+i*40,window,player_type) for j in range(10)]for i in range(10)]
        self._ships = []

    def get_ships(self):
        """
        Zwraca listę segmentów statków
        """
        return self._ships

    def draw_ship(self,position):
        """
        Rysowanie segmentu statku na podstawie położenia myszki
        """
        if self._player_type == PlayersType.PLAYER:
            for row in self._fields:
                for e in row:
                    if e.is_mouse_over(position):
                        return e.draw_ship_segment()

    def shot_i(self,position):
        """
        Analiza strzału
        """
        for x in range(10):
            for y in range(10):
                if self._fields[x][y].is_mouse_over(position):
                    return self.shot(x,y)


    def check_ships_position(self):
        """
        Sprawdza poprawność ułożenia statków na planszy
        """
        self._ships = []
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
                    if self._fields[i][j].get_field_state() == FieldStates.SHIP:
                        self._ships.append((i,j))
                        ship_len = 1
                        row = False
                        #statek w rzedzie
                        for k in range(1,5):
                            if j+k < 10:
                                if i_was_here[i][j+k] == 'yes' and self._fields[i][j+k].get_field_state() == FieldStates.SHIP:
                                    return False
                                if self._fields[i][j+k].get_field_state() == FieldStates.SHIP and j != 9:
                                    row = True
                                    i_was_here[i][j+k] = 'yes'
                                    self._ships.append((i,j+k))
                                    ship_len += 1
                                else:
                                    break
                        #statki w kolumnie
                        for k in range(1,5):
                            if i + k < 10:
                                if i_was_here[i+k][j] == 'yes' and self._fields[i+k][j].get_field_state() == FieldStates.SHIP:
                                    return False
                                if self._fields[i+k][j].get_field_state() == FieldStates.SHIP and i != 9:
                                    if row is True:
                                        return False
                                    i_was_here[i+k][j] = 'yes'
                                    self._ships.append((i+k,j))
                                    ship_len += 1
                                else:
                                    break
                        self._fields[i][j].change_text_with_new_color(str(ship_len),SEA_COLOR,self._window)
                        can_i = True
                        can_j = True
                        for p in range(ship_len):
                            if i+p < 10:
                                if self._fields[i+p][j].get_field_state() == FieldStates.SHIP and can_i:
                                    self._fields[i+p][j].change_text_with_new_color(str(ship_len), SEA_COLOR,
                                                                                  self._window)
                                else:
                                    can_i = False
                            if j + p < 10:
                                if self._fields[i][j+p].get_field_state() == FieldStates.SHIP and can_j:
                                    self._fields[i][j+p].change_text_with_new_color(str(ship_len), SEA_COLOR,
                                                                                          self._window)
                                else:
                                    can_j = False

                        if ship_len == 5:
                            return False
                        ships_pattern[ship_len] -= 1
                        #nie stykanie się nastepnych statków
                        for k in range(-1,ship_len+1):
                            if row is True:
                                if k+j != -1 and k+j != 10 and i != 9:
                                    if self._fields[i+1][j+k].get_field_state() == FieldStates.SHIP:
                                        return False
                                    else:
                                        i_was_here[i+1][j+k] = 'yes'
                            else:
                                if k+i != -1 and k+i != 10 and j != 9:
                                    if self._fields[i+k][j+1].get_field_state() == FieldStates.SHIP:
                                        return False
                                    else:
                                        i_was_here[i+k][j+1] = 'yes'
                                if k+i != -1 and k+i != 10 and j != 0:
                                    if self._fields[i+k][j-1].get_field_state() == FieldStates.SHIP:
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
        """
        Sprawdzenie wygranej
        """
        return len(self._ships) == 0

    def automatic_ships_generator(self):
        """
        Automatyczne generowanie pozycji statków
        """
        self._fields = [[Field(self._x_start + j * 40, self._y_start + i * 40, self._window, self._player_type) for j in range(10)] for i in range(10)]
        self._ships = []
        for i in range(4):
            self.generate_random_ship(4-i,i+1)

        self.check_ships_position()
        return True

    def can_add_ship(self,x,y,z,size):
        """
        Sprawdzenie możliwości dodania określonego statku w określone miejsce
        """
        if z == 0:
            for i in range(-1, size+1):
                if 0 <= x + i < 10:
                    if self._fields[x + i][y].get_field_state() == FieldStates.SHIP:
                        return False
                    if y+1 < 10:
                        if self._fields[x + i ][y+1].get_field_state() == FieldStates.SHIP:
                            return False
                    if y - 1 >= 0:
                        if self._fields[x + i ][y-1].get_field_state() == FieldStates.SHIP:
                            return False

        else:
            for i in range(-1, size+1):
                if 0 <= y + i < 10:
                    if self._fields[x][y + i].get_field_state() == FieldStates.SHIP:
                        return False
                    if x+1< 10:
                        if self._fields[x+1][y + i ].get_field_state() == FieldStates.SHIP:
                            return False
                    if x -1 >= 0:
                        if self._fields[x-1][y + i ].get_field_state() == FieldStates.SHIP:
                            return False
        return True

    def add_ship(self,x,y,z,size):
        """
        Dodanie statku do planszy
        """
        if z == 0:
            for i in range(size):
                self._fields[x + i][y].draw_ship_segment()
        else:
            for i in range(size):
                self._fields[x][y + i].draw_ship_segment()

    def shot(self,x,y):
        """
        Strzał
        """
        response = self._fields[x][y].hit()
        if response == 1:
            self._ships.remove((x,y))
        return response

    def generate_random_ship(self,size,numbers):
        """
        Wygenerowanie losowych statków
        """
        for _ in range(numbers):
            success = False
            while not success:
                x = random.randrange(11-size)
                y = random.randrange(11-size)
                z = random.randrange(2)
                success = self.can_add_ship(x, y, z, size)
                if success:
                    self.add_ship(x, y, z, size)


class Board_state(Enum):
    PREPARE = 0
    BATTLE = 1