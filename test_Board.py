from unittest import TestCase

from chess import Board, Move

from CustomBoard import CustomBoard
from LichessClient import LichessClient


class TestBoard(TestCase):
    def test_set_fen(self):
        board = CustomBoard()
        test_board = Board()

        test_board.push(Move.from_uci('e2e4'))
        board.set_fen(test_board.fen().split(' ')[0])

        test_board.push(Move.from_uci('e7e5'))
        board.set_fen(test_board.fen().split(' ')[0])
        last_fen = test_board.fen()

        test_board.push(Move.from_uci('g1f3'))
        board.set_fen(test_board.fen().split(' ')[0])

        test_board.push(Move.from_uci('b8c6'))
        board.set_fen(test_board.fen().split(' ')[0])

        test_board.push(Move.from_uci('f3g1'))
        board.set_fen(test_board.fen().split(' ')[0])

        test_board.push(Move.from_uci('c6b8'))
        board.set_fen(test_board.fen().split(' ')[0])

        test_board.push(Move.from_uci('d2d4'))
        board.set_fen(test_board.fen().split(' ')[0])

        test_board.push(Move.from_uci('f7f5'))
        board.set_fen(test_board.fen().split(' ')[0])

        # board.set_fen(last_fen.split(' ')[0])

        game = board.get_pgn()

        print(game)

        lichess_client = LichessClient()
        lichess_client.push_pgn_to_lichess(game.__str__())
