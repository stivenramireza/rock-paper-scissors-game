from src.models.player import Player
from src.models.game import Game


def main() -> None:
    nickname_1 = input('Enter the nicname for the player 1: ')
    player_1 = Player(nickname=nickname_1)

    nickname_2 = input('Enter the nicname for the player 2: ')
    player_2 = Player(nickname=nickname_2)

    game = Game(player_1, player_2)
    game.start()


if __name__ == '__main__':
    main()
