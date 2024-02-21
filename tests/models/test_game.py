import pytest

from src.models.game import Game
from src.models.player import Player


def test_game_validate_mode_failed() -> None:
    player_1 = Player(name='Test 1', nickname='test_1')
    player_2 = Player(name='Test 2', nickname='test_2')

    game = Game(player_1, player_2)

    with pytest.raises(Exception) as result:
        game.validate_mode('X')

    assert str(result.value) == 'Invalid mode, try again!'


def test_game_validate_mode_sucess() -> None:
    player_1 = Player(name='Test 1', nickname='test_1')
    player_2 = Player(name='Test 2', nickname='test_2')

    game = Game(player_1, player_2)

    result = game.validate_mode('PAPER')

    assert result == True
