from src.board import Board
import random


class Bot:
    def __init__(self,ships):
        """
        Inicjalizacja bota
        """
        self._ships = ships

    def shot(self):
        """
        Zwraca następny strzał bota
        """
        return random.randrange(10),random.randrange(10)