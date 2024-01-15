import time

from CustomBoard import CustomBoard
from DGT import DGTSync


class MainApp:
    def __init__(self) -> None:
        self.dgt_api = DGTSync()
        self.board = CustomBoard()

    def run(self):
        time.sleep(0.2)

        fen = self.dgt_api.get_fen()

        if fen is None:
            self.run()

        self.board.set_fen(fen)

        self.run()




if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()
