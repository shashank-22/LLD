from .Jumper import Jumper


class Ladder(Jumper):
    def __init__(self, head, tail):
        super().__init__(head=tail, tail=head)

    def __str__(self):
        return "Climb Ladder"

    @staticmethod
    def create_ladder(start, end):
        return Ladder(head=start, tail=end)

    def jump(self, player):
        player.position = self.head
