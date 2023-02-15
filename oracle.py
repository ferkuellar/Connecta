from enum import Enum, auto
from copy import deepcopy
from settings import BOARD_LENGTH
from square_board import SquareBoard
from settings import BOARD_LENGTH

class ColumnClassification(Enum):
    FULL    = -1    # imposible
    BAD     = 1     # muy indeseable
    MAYBE   = 10    # indeseable
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
    
    def no_good_options(self, board, player):
        #detecta que todas laas clasificaciones sean BAD o FULL
        # obtener las clasificaciones
        columnRecomendations = self.get_recommendation(board, player)
        # comprobamos que todas sean del tipo correcto
        result = True
        for rec in columnRecomendations:
            if (rec.classification == ColumnClassification.WIN) or (rec.classification == ColumnClassification.MAYBE):
                result = False
                break
        return result
    
class SmartOracle(BaseOracle):
    def _get_column_recommendation(self, board, index, player):
        # Afina la clasificacion de super e intenta encontrar columnas WIN

        recommendation = super()._get_column_recommendation(board, index, player)
        if recommendation.classification == ColumnClassification.MAYBE:
            #se puede mejorar
            if self._is_wining_move(board, index, player):
                recommendation.classification = ColumnClassification.WIN
            elif self._is_losing_move(board, index, player):
                recommendation.classification = ColumnClassification.BAD
        return recommendation
    
    def _is_losing_move(self, board, index, player):
        # si player juega en index ¿genera una jugada vencedora para el oponente en alguna de las columnas?

        tmp = self._play_on_tmp_board(board, index, player)

        will_lose = False
        for i in range(0, BOARD_LENGTH):
            if self._is_wining_move(tmp, i, player.opponent):
                will_lose = True
                break
        return will_lose
        
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
    
class MemoizingOracle(SmartOracle):
    # el metodo get_recommendaion esta ahora memoizado (cada vez qye te llaman guardas los parametros junto con el resultado de un diccionario)

    def __init__(self) -> None:
        super().__init__()
        self._past_recommendations = {}

    def _make_key(self, board_code, player):
        # la clave debe combinar el board y el player de la forma mas sencilla posible
        return f'{board_code.raw_code}@{player.char}'

    def get_recommendation(self, board, player):
        # creamos la clave
        key = self._make_key(board.as_code(), player)
        # Miramos en el cache: si no esta calculo y guardo en cache
        if key not in self._past_recommendations:
            self._past_recommendations[key] = super().get_recommendation(board, player)
        # devuelve lo que esta en el cache
        return self._past_recommendations[key]
    
class LearningOracle(MemoizingOracle):
    
    def update_to_bad(self, board_code, player, position):
        # crear clave
        key = self._make_key(board_code, player)
        # obtener la clasificiacion erronea
        recommendation = self.get_recommendation(SquareBoard.fromBoardCode(board_code), player)
        # corregirla
        recommendation[position] = ColumnRecommendation(position, ColumnClassification.BAD)
        # sustituirla
        self._past_recommendations[key] = recommendation