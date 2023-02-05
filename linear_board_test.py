import pytest
from linear_board import *
from settings import BOARD_LENGTH, VICTORY_STRIKE

def test_empty_board():
    empty = LinearBoard()
    assert empty != None
    assert empty.is_full() == False
    assert empty.is_victory('X') == False


def test_add():
    b = LinearBoard()
    for i in range(BOARD_LENGTH):
        b.add('X')
    assert b.is_full() == True

def test_victory():
    b = LinearBoard()
    for i in range(VICTORY_STRIKE):
        b.add('X')
    assert b.is_victory('O') == False
    assert b.is_victory('X') == True
    
def test_tie():
    b = LinearBoard()

    b.add('O')
    b.add('O')
    b.add('X')
    b.add('O')

    assert b.is_tie('X', 'O')

def test_add_to_full():
    full = LinearBoard()
    for i in range(BOARD_LENGTH):
        full.add('x')
    full.add('X')
    assert full.is_full()