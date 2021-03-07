from .Jumper import Jumper


class Snake(Jumper):
    def __init__(self, head, tail):
        super().__init__(head=head, tail=tail)

    def __str__(self):
        return "Snake Bite"

    @classmethod
    def create_snake(cls, start, end):
        return cls(head=start, tail=end)

    def jump(self, player):
        player.position = self.tail

