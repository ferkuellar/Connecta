import pyfiglet
from enum import Enum, auto
from match import Match
from player import Player
from square_board import SquareBoard

class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()

class DifficultyLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

class Game():

    def __init__(self, 
                round_type = RoundType.COMPUTER_VS_COMPUTER,
                match = Match(Player('Chip'), Player('Chop'))):
        # Guardar valores repetidos
        self.round_type = round_type
        # Tablero vacio sobre el que jugar
        self.board = SquareBoard()
    
    def start(self):
        # imprimo el nombre o logo del juego
        self.print_logo()
        # configuro la partida
        # arranco el game loop

    def print_logo(self):
        logo = pyfiglet.Figlet(font = 'stop')
        print(logo.renderText('Connecta'))
