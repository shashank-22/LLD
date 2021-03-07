from Game import Game
from GameResources.Player import Player

if __name__ == "__main__":
    game = Game.create_game()

    player1 = Player.create_player(name="Alice")
    player2 = Player.create_player(name="BoB")

    game.start_game(players=[player1, player2])


