import pyfiglet
from enum import Enum, auto
from match import Match
from player import Player, HumanPlayer
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
            if self._is_game_over():
                # muestra el resultado final 
                self._display_result()
                # salgo del bucle
                break

    def _display_move():
        pass

    def _display_board():
        pass

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

    def _display_result():
        pass

    def _configure_by_user(self):
        # Le pido al usuario, los valores que el quiere para tipo de partoda y nivel de dificultad
        # determina el tipo de partida (pregunatndo al usuario)
        self.round_type = self._get_round_type()

        # crear la partida
        self.match = self._make_match()

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

    def _make_match(self):
        # PLayer 1 siempre robotico

        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            #son los jugaodres roboticos
            player1 = Player('T-X')
            player2 = Player('T-1000')
        else:
            # ord vs humano
            player1 = Player('T-800')
            player2 = HumanPlayer(name = input('Enter your name, puny, Human: '))

        return Match(player1, player2)
