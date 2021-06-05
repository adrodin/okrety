import random
from src.field import Field
from src.board import Board

class MediumMode:
    def __init__(self,ships):
        """
        Inicjalizacja trudnego bota
        """
        self._ships = ships
        self._next_shot = []

    def shot(self):
        """
        Zwraca następny strzał bota
        """
        if len(self._next_shot) == 0:
            x = random.randrange(10)
            y = random.randrange(10)
            self._next_shot.append((x,y))
            if (x, y) in self._ships:
                for i in range(3):
                    if (x + i + 1, y) in self._ships:
                        self._next_shot.append((x+i+1,y))
                    else:
                        break
                for i in range(3):
                    if (x - i - 1, y) in self._ships:
                        self._next_shot.append((x-i-1,y))
                    else:
                        break
                for i in range(3):
                    if (x, y + i + 1) in self._ships:
                        self._next_shot.append((x,y+i+1))
                    else:
                        break
                for i in range(3):
                    if (x, y - i - 1) in self._ships:
                        self._next_shot.append((x,y-i-1))
                    else:
                        break
        return self._next_shot.pop(0)

