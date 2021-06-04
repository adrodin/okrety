from src.field import Field
from src.board import Board

class SniperMode:
    def __init__(self,ships):
        self._ships = ships

    def shot(self):
        return self._ships[0][0],self._ships[0][1]