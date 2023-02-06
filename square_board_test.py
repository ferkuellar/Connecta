import pytest

from square_board import *

def test_empty_board():
    board = SquareBoard()

    assert board.is_full() == False
    assert board.is_victory('O') == False
    assert board.is_victory('X') == False

def test_vertical_victory():
    vertical = SquareBoard.fromList([['O', 'X', 'X', 'X',
                                    [None, None, None, None, ],
                                    [None, None, None, None, ],
                                    [None, None, None, None, ],
                                    [None, None, None, None, ]]])
    assert vertical.is_victory('X')
    assert vertical.is_victory('O') == False

def test_horizontal_victory():
    horizontal_victory = SquareBoard.fromList([['X', None, None, None, None, ],
                                                ['X', None, None, None, None, ],
                                                ['X', 'O', None, None, None, ],
                                                ['X', 'O', None, None, None, ],
                                                ['X', 'O', None, None, None, ]])
    assert horizontal_victory.is_victory('X')

def test_sinking_victory():
    sinking_victory = SquareBoard.fromList([['X', 'O', 'X', 'O', ],
                                            ['X' , 'X', 'O', None, ],
                                            ['O', 'O', None, None, ],
                                            ['O', 'X', None, None, ],
                                            ['X', None, None, None, ]])
    assert sinking_victory.is_victory('O')
    assert sinking_victory.is_victory('X') == False

def test_rising_victory():
    rising_victory = SquareBoard.fromList([['X', 'O', None, None, ],
                                            ['O', 'X', None, None, ],
                                            ['X', 'O', 'X', 'O', ],
                                            ['X', 'O', 'O', 'X', ],
                                            ['O', 'X', 'O', None, ]])
    assert rising_victory.is_victory('X')
    assert rising_victory.is_victory('O') == False