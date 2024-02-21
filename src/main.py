from models.player import Player
from models.game import Game


def main() -> None:
    player_1 = Player(name='Stiven Ramírez Arango', nickname='stivenramireza')
    player_2 = Player(name='Julián David Ramírez Arango', nickname='juliandavram')

    game = Game(player_1, player_2)
    game.start()


if __name__ == '__main__':
    main()
