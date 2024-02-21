from enum import Enum

from models.player import Player
from utils.logger import logger


class Mode(Enum):
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'


class Game:
    player_1: Player
    player_2: Player
    tries: int
    counter_1: int
    counter_2: int
    result: dict[Player, int]
    DEFAULT_TRIES: int = 3

    def __init__(self, player_1: Player, player_2: Player) -> None:
        self.player_1 = player_1
        self.player_2 = player_2
        self.tries = 0
        self.counter_1 = 0
        self.counter_2 = 0
        self.result = dict()

    def __str__(self) -> str:
        return 'Game setup'

    def _get_game_winner(self) -> Player:
        return max(self.result, key=self.result.get) if self.result else None

    def _get_play_winner(self) -> dict[tuple, Mode]:
        return {
            tuple[Mode.ROCK.value, Mode.PAPER.value]: Mode.PAPER.value,
            tuple[Mode.ROCK.value, Mode.SCISSORS.value]: Mode.ROCK.value,
            tuple[Mode.PAPER.value, Mode.ROCK.value]: Mode.PAPER.value,
            tuple[Mode.PAPER.value, Mode.SCISSORS.value]: Mode.SCISSORS.value,
            tuple[Mode.SCISSORS.value, Mode.ROCK.value]: Mode.ROCK.value,
            tuple[Mode.SCISSORS.value, Mode.PAPER.value]: Mode.SCISSORS.value,
        }

    def _validate_play(
        self, player_1_play: dict[str, str], player_2_play: dict[str, str]
    ) -> None:
        play_1, play_2 = player_1_play.get(self.player_1), player_2_play.get(
            self.player_2
        )

        play_winner = self._get_play_winner()

        play_result = play_winner.get(tuple[play_1, play_2])
        if play_1 == play_result:
            self.counter_1 += 1
            self.result[self.player_1] = self.counter_1
        else:
            self.counter_2 += 1
            self.result[self.player_2] = self.counter_2

    def _validate_mode(self, trie: str) -> bool:
        modes = [mode.value for mode in Mode]
        if trie not in modes:
            raise Exception('Invalid mode, try again!')

        return True

    def start(self) -> None:
        logger.info('Welcome to the rock-paper-scissors game!')

        while self.tries < self.DEFAULT_TRIES:
            trie_1 = input(
                f'- Type the mode for the player {self.player_1.nickname}: '
            )
            self._validate_mode(trie_1)
            trie_2 = input(
                f'- Type the mode for the player {self.player_2.nickname}: '
            )
            self._validate_mode(trie_2)

            if trie_1 == trie_2:
                self.tries += 1
                continue

            player_1_play, player_2_play = {self.player_1: trie_1}, {
                self.player_2: trie_2
            }
            self._validate_play(player_1_play, player_2_play)

            self.tries += 1

        winner = self._get_game_winner()

        if winner:
            logger.info(
                f'The winner was {winner} with {self.result.get(winner)} tries'
            )
        else:
            logger.info('No winner!')

        logger.info('End game!')
