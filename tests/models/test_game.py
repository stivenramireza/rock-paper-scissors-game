import pytest
from unittest.mock import patch

from src.models.game import Game, Mode
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


def test_game_get_play_winner() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')
    game = Game(player_1, player_2)

    # Act
    play_winner = game._get_play_winner()

    # Assert
    assert play_winner[tuple[Mode.ROCK, Mode.PAPER]] == Mode.PAPER
    assert play_winner[tuple[Mode.ROCK, Mode.SCISSORS]] == Mode.ROCK
    assert play_winner[tuple[Mode.PAPER, Mode.ROCK]] == Mode.PAPER
    assert play_winner[tuple[Mode.PAPER, Mode.SCISSORS]] == Mode.SCISSORS
    assert play_winner[tuple[Mode.SCISSORS, Mode.ROCK]] == Mode.ROCK
    assert play_winner[tuple[Mode.SCISSORS, Mode.PAPER]] == Mode.SCISSORS


def test_game_start_player_1_wins() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')
    game = Game(player_1, player_2)

    # Mock user inputs: player_1 always wins
    inputs = [
        'PAPER',
        'ROCK',  # Round 1: PAPER beats ROCK
        'PAPER',
        'ROCK',  # Round 2: PAPER beats ROCK
        'PAPER',
        'ROCK',  # Round 3: PAPER beats ROCK
    ]

    # Act
    with patch('builtins.input', side_effect=inputs), patch(
        'src.utils.logger.logger.info'
    ) as mock_logger:
        game.start()

    # Assert
    assert game.counter_1 == 3
    assert game.counter_2 == 0
    assert game._get_game_winner() == player_1
    mock_logger.assert_called()


def test_game_start_player_2_wins() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')
    game = Game(player_1, player_2)

    # Mock user inputs: player_2 always wins
    inputs = [
        'ROCK',
        'PAPER',  # Round 1: PAPER beats ROCK
        'ROCK',
        'PAPER',  # Round 2: PAPER beats ROCK
        'ROCK',
        'PAPER',  # Round 3: PAPER beats ROCK
    ]

    # Act
    with patch('builtins.input', side_effect=inputs), patch(
        'src.utils.logger.logger.info'
    ) as mock_logger:
        game.start()

    # Assert
    assert game.counter_1 == 0
    assert game.counter_2 == 3
    assert game._get_game_winner() == player_2
    mock_logger.assert_called()


def test_game_start_with_ties() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')
    game = Game(player_1, player_2)

    # Mock user inputs: with ties that get skipped
    # Note: ties increment tries counter, so we need extra rounds
    inputs = [
        'ROCK',
        'ROCK',  # Tie (tries becomes 1, continue)
        'PAPER',
        'ROCK',  # Round 1: PAPER beats ROCK (player_1 wins, tries becomes 2)
        'ROCK',
        'PAPER',  # Round 2: PAPER beats ROCK (player_2 wins, tries becomes 3)
    ]

    # Act
    with patch('builtins.input', side_effect=inputs), patch(
        'src.utils.logger.logger.info'
    ) as mock_logger:
        game.start()

    # Assert
    assert game.tries == 3
    assert game.counter_1 == 1
    assert game.counter_2 == 1
    assert game._get_game_winner() == player_1  # When tied, player_1 is returned by max()
    mock_logger.assert_called()


def test_game_start_no_winner() -> None:
    # Arrange
    player_1 = Player(nickname='test_1')
    player_2 = Player(nickname='test_2')
    game = Game(player_1, player_2)

    # Mock user inputs: all ties - game should end with no winner
    inputs = [
        'ROCK',
        'ROCK',  # Tie (skipped)
        'PAPER',
        'PAPER',  # Tie (skipped)
        'SCISSORS',
        'SCISSORS',  # Tie (skipped)
    ]

    # Act
    with patch('builtins.input', side_effect=inputs), patch(
        'src.utils.logger.logger.info'
    ) as mock_logger:
        game.start()

    # Assert
    assert game.counter_1 == 0
    assert game.counter_2 == 0
    assert game._get_game_winner() is None
    mock_logger.assert_called()
