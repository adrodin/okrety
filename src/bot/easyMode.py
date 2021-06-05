import random
from src.field import Field
from src.board import Board
from src.bot.bot import Bot


class EasyMode(Bot):
    def __init__(self,ships):
        """
        Inicjalizacja łatwego bota
        """
        super().__init__(ships)


