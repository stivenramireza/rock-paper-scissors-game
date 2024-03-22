import pytest

from src.models.game import Game
from src.models.player import Player


def test_game_str() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')

    game = Game(player_1, player_2)

    # Assert
    assert str(game) == 'Game setup'


def test_game_validate_mode_failed() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')

    game = Game(player_1, player_2)

    # Act
    with pytest.raises(Exception) as result:
        game._validate_mode('X')

    # Assert
    assert str(result.value) == 'Invalid mode, try again!'


def test_game_validate_mode_sucess() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')

    game = Game(player_1, player_2)

    # Act
    result = game._validate_mode('PAPER')

    # Assert
    assert result == True


def test_game_validate_play_player_1() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')

    game = Game(player_1, player_2)

    player_1_play, player_2_play = {player_1: 'PAPER'}, {player_2: 'ROCK'}

    # Act
    game._validate_play(player_1_play, player_2_play)

    # Assert
    assert game.result == {player_1: 1}


def test_game_validate_play_player_2() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')

    game = Game(player_1, player_2)

    player_1_play, player_2_play = {player_1: 'SCISSORS'}, {player_2: 'ROCK'}

    # Act
    game._validate_play(player_1_play, player_2_play)

    # Assert
    assert game.result == {player_2: 1}


def test_game_get_game_winner_player_1() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')

    game = Game(player_1, player_2)

    player_1_play, player_2_play = {player_1: 'PAPER'}, {player_2: 'ROCK'}

    # Act
    game._validate_play(player_1_play, player_2_play)
    result = game._get_game_winner()

    # Assert
    assert result == player_1
