import pytest
from player import Player, HumanPlayer
from match import Match
from square_board import SquareBoard

fernando = None
otto = None

def setup():
    global fernando
    fernando = HumanPlayer('Fernando')
    global otto
    otto = Player('Dr Cuellar')

def teardown():
    global fernando
    fernando = None
    global otto
    otto = None

def test_different_players_have_different_chars():
    t = Match(fernando, otto)
    assert fernando.char != otto.char

def test_no_player_with_none_char():
    t = Match(fernando, otto)
    assert fernando.char != None
    assert otto.char != None

def test_netx_player_is_round_robbin():
    t = Match(otto, fernando)
    p1 = t.next_player
    p2 = t.next_player
    assert p1 != p2

