from GameResources.GameBoard import GameBoard
from GameResources.Snake import Snake
from GameResources.Ladder import Ladder
from GameResources.Dice import Dice
import sys
import time


class Game:
    def __init__(self, board, dice):
        self.board = board
        self.dice = dice

    @classmethod
    def create_game(cls):
        snakes = [
            Snake.create_snake(start=35, end=3),
            Snake.create_snake(start=99, end=2),
            Snake.create_snake(start=70, end=45),
            Snake.create_snake(start=20, end=1),
            Snake.create_snake(start=56, end=20)
        ]

        ladders = [
            Ladder.create_ladder(start=4, end=38),
            Ladder.create_ladder(start=22, end=98),
            Ladder.create_ladder(start=50, end=89),
            Ladder.create_ladder(start=10, end=21),
            Ladder.create_ladder(start=76, end=91)
        ]

        dice = Dice.create_dice()
        board = GameBoard.create_board(jumpers=snakes+ladders)
        return cls(board=board, dice=dice)

    @staticmethod
    def show_player_position(player, move):
        print("[Dice: {2}] {0} is at {1} position".format(player.name, player.position, move))

    @staticmethod
    def jump_if_possible(board, player):
        prev_position = player.position
        if prev_position in board.jumperMap:
            jumper = board.jumperMap.get(prev_position)
            jumper.jump(player)
            print("*******************************")
            print("{} for {}: Moved from {} to {}".format(
                jumper, player.name, prev_position, player.position))
            print("*******************************")
        if player.position < 1 or player.position > 100:
            raise

    @staticmethod
    def declear_winner(player):
        print("{0} won the game".format(player.name))

    @staticmethod
    def end_game():
        print("Game end")
        sys.exit(0)

    def start_game(self, players):
        board = self.board

        while 1:
            for player in players:
                # time.sleep(1)
                move = self.dice.roll

                if player.position + move < 100:
                    player.move_player(move)
                    self.show_player_position(player=player, move=move)
                    self.jump_if_possible(board=board, player=player)

                elif player.position + move == 100:
                    player.move_player(move)
                    self.show_player_position(player=player, move=move)
                    self.declear_winner(player)
                    self.end_game()

                else:
                    print(
                        "[Dice: {}] {} can't move further will retry".format(
                            move, player.name))
