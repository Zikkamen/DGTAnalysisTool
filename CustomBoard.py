import chess.pgn
from chess import Board


class CustomBoard:
    def __init__(self):
        self.board = Board()
        self.game = chess.pgn.Game()
        self.node = self.game.root()
        self.fen_to_node = {'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR': self.node}

    def set_fen(self, fen):
        if fen == 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR':
            self.__init__()
            return

        for move in self.board.legal_moves:
            self.board.push(move)

            if fen == self.board.fen().split(' ')[0]:
                self.node = self.node.add_variation(move)

                if fen not in self.fen_to_node:
                    self.fen_to_node[fen] = self.node

                return

            self.board.pop()

        if fen in self.fen_to_node:
            self.node = self.fen_to_node[fen]
            self.board = self.node.board()

    def set_board(self, game_board):
        self.board = game_board

    def get_pgn(self):
        if self.node.next() is not None:
            self.node.remove_variation(self.node.next())

        return self.game


if __name__ == "__main__":
    board = CustomBoard()
    board.set_fen("")
