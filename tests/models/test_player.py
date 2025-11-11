from src.models.player import Player


def test_player_str_() -> None:
    # Arrange
    player = Player(nickname='test')

    # Assert
    assert str(player) == 'test'


def test_player_init() -> None:
    # Arrange
    nickname = 'player_one'

    # Act
    player = Player(nickname=nickname)

    # Assert
    assert player.nickname == nickname
