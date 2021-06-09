from src.board import Board
import random


class Bot:
    def __init__(self,ships):
        """
        Inicjalizacja bota
        :param ships: lista staków do zestrzelenia
        """
        self._ships = ships

    def shot(self):
        """
        Zwraca następny strzał bota
        :return: x, y - strzał bota
        """
        return random.randrange(10),random.randrange(10)