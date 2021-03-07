import random


class Dice:
    def __init__(self, faces=6):
        self.faces = faces

    @classmethod
    def create_dice(cls):
        return cls()

    @property
    def roll(self):
        return random.randint(1, self.faces)
