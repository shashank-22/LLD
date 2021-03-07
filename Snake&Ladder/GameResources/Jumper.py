from abc import abstractmethod


class Jumper:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    @abstractmethod
    def jump(self, player):
        pass
