class Player:
    nickname: str

    def __init__(self, nickname: str):
        self.nickname = nickname

    def __str__(self) -> str:
        return self.nickname
