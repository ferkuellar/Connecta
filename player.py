from oracle import BaseOracle, ColumnClassification, ColumnRecommendation
import random
from list_utils import all_same
from move import Move
from settings import BOARD_LENGTH
from beautifultable import BeautifulTable


class Player():
    # juega en un tablero despues de preguntar al oraculo

    def __init__(self, name, char = None, opponent = None, oracle=BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle
        self.opponent = opponent
        self.last_move = None

    @property
    def opponent(self):
        return self._opponent
    
    @opponent.setter
    def opponent(self, other):
        if other != None:
            self._opponent = other
            other._opponent = self

    def play(self, board):
        # Elije la mejor columna de aquellas que recomienda el oraculo

        # Pregunto al oraculo () primeros es una tupla
        (best, recommendations) = self._ask_oracle(board)
        # Juego en la mejor
        self._play_on(board, best.index, recommendations)

    def on_win(self):
        pass

    def on_lose(self):
        pass

    def _play_on(self, board, position, recomendations):
        # juega en la posicion
        board.add(self.char, position)
        # guardo mi ultima jugada
        self.last_move = Move(position, board.as_code(), recomendations, self)

    def _ask_oracle(self, board):
        # pregunta al oraculo y devuelve la mejor opcion

        # obtenemos las recomendaciones
        recommendation = self._oracle.get_recommendation(board, self)
        # seleccionamos la mejor
        best = self._choose(recommendation)
        return(best, recommendation)

    def _choose(self, recomendations):
        # Quitamos la no validas
        valid = list(filter(lambda x : x.classification != ColumnClassification.FULL, recomendations))
        # ordenamos por el valor de clasificiacion
        valid = sorted(valid, key=lambda x: x.classification.value, reverse=True)
        # si son todas iguales, agarro una al azar
        if all_same(valid):
            return random.choice(valid)
        else:
        # si no lo son todas iguales agarro la mas deseable(que sera la primera)
            return valid[0]  

class HumanPlayer(Player):
    def __init__(self, name, char = None):
        super().__init__(name, char)

    def _ask_oracle(self, board):
        # Le pido al humano que es mi oraculo

        while True:
            # pedimos columna al humano
            raw = input('Select a column, puny Human: ')
            #verificacmos que su respuesta sno sea una pendejada
            if _is_int(raw) and _is_within_column_range(board, int(raw)) and _is_non_full_column(board, int(raw)):
                # si no lo es, jugamos donde ha dicho y salimos del bucle
                pos = int(raw)
                return(ColumnRecommendation(pos, None), None)

class ReportingPlayer(Player):

    def on_lose(self):
        # le pide al oraculo que revise sus recomendaciones

        board_code = self.last_move.board_code
        position = self.last_move.position
        self._oracle.update_to_bad(board_code, self, position)


# funciones de validacion de indice de columna

def _is_non_full_column(board, num):
    return not board._columns[num].is_full()

def _is_within_column_range(board, num):
    return num >= 0 and num < len(board)

def _is_int(aString):
    try:
        num = int(aString)
        return True
    except:
        return False
    