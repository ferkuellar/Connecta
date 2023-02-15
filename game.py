import pyfiglet
from beautifultable import BeautifulTable
from oracle import SmartOracle, BaseOracle, LearningOracle
from settings import BOARD_LENGTH
from square_board import SquareBoard
from match import Match
from list_utils import reverse_matrix
from player import ReportingPlayer, HumanPlayer
from enum import Enum, auto


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
                match = Match(ReportingPlayer('Chip'), ReportingPlayer('Chop'))):
        # Guardar valores repetidos
        self.round_type = round_type
        # Tablero vacio sobre el que jugar
        self.board = SquareBoard()
    
    def start(self):
        # imprimo el nombre o logo del juego
        self.print_logo()
        # configuro la partida
        self._configure_by_user()
        # arranco el game loop
        self._start_game_loop()

    def print_logo(self):
        logo = pyfiglet.Figlet(font = 'stop')
        print(logo.renderText('Connecta'))

    def _start_game_loop(self):
        # bucle infinito
        while True:
            # obtengo el jugador de turno
            current_player = self.match.next_player
            # le hago jugar
            current_player.play(self.board)
            # muestro la jugada
            self._display_move(current_player)
            # imprimo el tablero
            self._display_board()
            # si el juego ha terminado....
            if self._has_winner_or_tie():
                # muestra el resultado final 
                self._display_result()
                # salgo del bucle
                break

    def _display_move(self, player):
        print(f'\n{player.name} ({player.char}) has move in column {player.last_move[0].position}')

    def _display_board(self):
        # imprirmir el tablero en su estado actual
        #obtenemos una matriz de caracteres a partir del tablero
        matrix = self.board.as_matrix()
        matrix = reverse_matrix(matrix)
        #crear la tabla de beatifultable
        bt = BeautifulTable()
        for col in matrix:
            bt.columns.append(col)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]
        # Imprimirla
        print(bt)

    def _is_game_over(self):
        # el juego se acaba cuando hay vencedor
        winner = self.match.get_winner(self.board)
        if winner != None:
            # hay un vencedor
            return True
        elif self.board.is_full():
            #empate
            return True
        else:
            return False

    def _display_result(self):
        winner = self.match.get_winner(self.board)
        if winner != None:
            print (f'\n{winner.name} ({winner.char}) wins!!!')
        else:
            print(f'\nA tie between {self.match.get_player("x"). name} (x) and {self.match.get_player("o").name}')


    def _configure_by_user(self):
        # Le pido al usuario, los valores que el quiere para tipo de partoda y nivel de dificultad
        # determina el tipo de partida (pregunatndo al usuario)
        self.round_type = self._get_round_type()

        # preguntamos nivel de dificultad
        if self.round_type == RoundType.COMPUTER_VS_HUMAN:
            self._difficulty_level = self._get_difficulty_level()

        # crear la partida
        self.match = self._make_match()

    def _get_difficulty_level(self):
        #pregunta al ususario como de listo sea el oponente
        print("""
        Chose your opponent, Humano:
        1) Bender: for clowns an wimps
        2) T-800 : you may get regret it
        3) T-1000: Don´t even think about it!!!
        """)
        while True:
            response = input('Please type 1, 2 or 3: ').strip()
            if response == '1':
                level = DifficultyLevel.LOW
                break
            elif response == '2':
                level = DifficultyLevel.MEDIUM
                break
            else:
                level = DifficultyLevel.HIGH
                break
        return level
            

    def _make_match(self):
        # PLayer 1 siempre robotico
        _levels = {DifficultyLevel.LOW : BaseOracle(), 
                    DifficultyLevel.MEDIUM : SmartOracle,
                    DifficultyLevel.HIGH : LearningOracle()}
        
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            #son los jugaodres roboticos
            player1 = ReportingPlayer('T-X', oracle = LearningOracle())
            player2 = ReportingPlayer('T-1000', oracle = LearningOracle())
        else:
            # ordenador vs humano
            player1 = ReportingPlayer('T-800', oracle=_levels[self._difficulty_level])
            player2 = HumanPlayer(name = input('Enter your name, puny, Human: '))

        # creamos la partida
        return Match(player1, player2)


    def _get_round_type(self):
        # Preguntar al usuario

        print( """Selecciona el tipo de round:

                1) COMPUTER VS COMPUTER
                2) COMPUTER VS HUMAN
        """)

        response = ''
        while response != "1" and response != "2":
            response = input('Please type either 1 or 2: ')
        if response == '1':
            return RoundType.COMPUTER_VS_COMPUTER
        else:
            return RoundType.COMPUTER_VS_HUMAN

