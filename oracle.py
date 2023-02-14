from enum import Enum, auto
from copy import deepcopy
from square_board import SquareBoard
from settings import BOARD_LENGTH

class ColumnClassification(Enum):
    FULL    = -1    # imposible
    MAYBE   = 1     # indeseable
    WIN     = 100   # La mejor opcion: gano por mucho

class ColumnRecommendation():
    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

    def __eq__(self, other):
        # si son de clases distatintas, pues son distintos
        if not isinstance(other, self.__class__):
            return False
        # solo importa la clasificacion
        else:
            return self.classification == other.classification
        
    def __hash__(self) -> int:
        return hash((self.index, self.classification))
    
    def __repr__(self):
        return f'{self.__class__}:{self.classification}'

class BaseOracle():

    def get_recommendation(self, board, player):
        # Returns a list of ColumnRecommendations
        
        recommendations = []
        for i in range(len(board)):
            recommendations.append(
                self._get_column_recommendation(board, i, player))
        return recommendations
    

    def _get_column_recommendation(self, board, index, player):
        # Classifies a column as either FULL or MAYBE and returns an ColumnRecommendation
        
        classification = ColumnClassification.MAYBE
        if board._columns[index].is_full():
            classification = ColumnClassification.FULL

        return ColumnRecommendation(index, classification)
    
class SmartOracle(BaseOracle):
    def _get_column_recommendation(self, board, index, player):
        # Afina la clasificacion de super e intenta encontrar columnas WIN

        recommendation = super()._get_column_recommendation(board, index, player)
        if recommendation.classification == ColumnClassification.MAYBE:
            #se puede mejorar
            recommendation = self._is_wining_move(board, index, player)
            return recommendation
        
    def _is_wining_move(self, board, index, player):
        # determina si al jugar una posicion, nos llevaria a ganar de inmediato

        # hago una copia del tablero        
        # juego en ella
        tmp = self._play_on_tmp_board(board, index, player)
        # determino si no hay una victoria para player o no
        return tmp.is_victory(player.char)
    
    def _play_on_tmp_board(self, board, index, player):
        # crea una copia del board y juega en el 
        tmp = deepcopy(board)

        tmp.add(player.char, index)

        #devuelvo la copia alterada
        return tmp