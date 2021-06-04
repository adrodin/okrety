import random
from src.field import Field
from src.board import Board


class EasyMode:
    def __init__(self,ships):
        self._ships = ships

    def shot(self):
        x = random.randrange(10)
        y = random.randrange(10)
        return x,y