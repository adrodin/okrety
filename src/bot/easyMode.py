import random
from src.field import Field
from src.board import Board


class EasyMode:
    def __init__(self,ships):
        """
        Inicjalizacja łatwego bota
        """
        self._ships = ships

    def shot(self):
        """
        Zwraca następny strzał łatwego bota
        """
        x = random.randrange(10)
        y = random.randrange(10)
        return x,y