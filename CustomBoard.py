import chess.pgn
from chess import Board


class CustomBoard:
    def __init__(self):
        self.game = chess.pgn.Game()
        self.node = self.game.root()
        self.fen_to_node = {'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR': self.node}

    def set_fen(self, fen):
        if fen == 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR':
            self.__init__()
            return

        temp_board = self.node.board()

        for move in temp_board.legal_moves:
            temp_board.push(move)

            if fen == temp_board.fen().split(' ')[0]:
                self.node = self.node.add_variation(move)

                if fen not in self.fen_to_node:
                    self.fen_to_node[fen] = self.node

                return

            temp_board.pop()

        if self.node.parent is not None:
            temp_board = self.node.parent.board()

            for move in temp_board.legal_moves:
                temp_board.push(move)

                if fen == temp_board.fen().split(' ')[0]:
                    print(temp_board.fen(), "found previous board legal move")
                    self.node = self.node.parent
                    self.node.remove_variation(self.node.next())
                    self.node = self.node.add_variation(move)

                    if fen not in self.fen_to_node:
                        self.fen_to_node[fen] = self.node

                    return

                temp_board.pop()

        if fen in self.fen_to_node:
            self.node = self.fen_to_node[fen]


    def get_pgn(self):
        if self.node.next() is not None:
            self.node.remove_variation(self.node.next())

        return self.game


if __name__ == "__main__":
    board = CustomBoard()
    board.set_fen("")
