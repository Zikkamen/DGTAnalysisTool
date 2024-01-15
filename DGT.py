import re
import time

from CustomBoard import CustomBoard


def call() -> str:
    # r = requests.get("http://localhost:1982/api/v1.0/eboards")

    text = '"board" : "rnbqkbnr/pppppppp/8/P7/8/8/1PPPPPPP/RNBQKBNR"'
    return re.findall('"board" : "([A-Za-z0-9/ -]*)"', text)[0]


class DGTSync:
    def __init__(self) -> None:
        self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.last_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

        self.board = CustomBoard()

    def get_fen(self) -> str | None:
        self.fen = call()

        time.sleep(0.2)

        if self.last_fen == self.fen:
            return

        self.last_fen = self.fen
        return self.fen
