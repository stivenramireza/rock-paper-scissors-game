class Player:
    name: str
    nickname: str

    def __init__(self, name: str, nickname: str):
        self.name = name
        self.nickname = nickname

    def __str__(self) -> str:
        return self.nickname
