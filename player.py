from oracle import BaseOracle, ColumnClassification, ColumnRecommendation 


class Player():
    # juega en un tablero despues de preguntar al oraculo

    def __init__(self, name, char=None, oracle=BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle

    def play(self, board):
        # recomdendaciones del oraculo
        # selecciono la mejor opcion
        # juego en ella
        pass

    def _chose(self, recomendations):
        # seleccionar la mejor opcion de la lista
        # de recomendaciones
        pass