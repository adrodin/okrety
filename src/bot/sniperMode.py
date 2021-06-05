from src.field import Field
from src.board import Board

class SniperMode:
    def __init__(self,ships):
        """
        Inicjalizacja snajpera
        """
        self._ships = ships

    def shot(self):
        """
        Zwraca następny strzał snajpera
        """
        return self._ships[0][0],self._ships[0][1]