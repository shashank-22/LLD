from GameResources.Snake import Snake
from GameResources.Ladder import Ladder


class GameBoard:
    def __init__(self, jumpers, size=100):
        self.size = size
        self.jumpers = jumpers
        self.jumperMap = {}

    @classmethod
    def create_board(cls, jumpers):
        board = cls(jumpers=jumpers)
        board._create_map()
        return board

    def _create_map(self):
        for jumper in self.jumpers:
            if isinstance(jumper, Snake):
                self.jumperMap[jumper.head] = jumper
            elif isinstance(jumper, Ladder):
                self.jumperMap[jumper.tail] = jumper
            else:
                raise
