class Player:
    def __init__(self, name, position=0):
        self.name = name
        self.position = position

    @classmethod
    def create_player(cls, name):
        return cls(name=name)

    def move_player(self, move):
        self.position += move


