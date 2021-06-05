from src.field import Field
from src.board import Board
from src.bot.bot import Bot

class SniperMode(Bot):
    def __init__(self,ships):
        """
        Inicjalizacja snajpera
        """
        super().__init__(ships)

    def shot(self):
        """
        Zwraca następny strzał snajpera
        """
        return self._ships[0][0],self._ships[0][1]