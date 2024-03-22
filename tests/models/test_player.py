from src.models.player import Player


def test_player_str_() -> None:
    # Arrange
    player = Player(nickname='test')

    # Assert
    assert str(player) == 'test'
