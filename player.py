from oracle import BaseOracle, ColumnClassification, ColumnRecommendation 


class Player():
    # juega en un tablero despues de preguntar al oraculo

    def __init__(self, name, char, oracle=BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle

    def play(self, board):
        # recomdendaciones del oraculo
        recommendations = self._oracle.get_recommendation(board, self)
        # selecciono la mejor opcion
        best = self._choose(recommendations)
        # juego en ella
        board.add(self.char, best.index)

    def _choose(self, recomendations):
        # Quitamos la no validas
        valid = list(filter(lambda x : x.classification != ColumnClassification.FULL, recomendations))
        # Agarramos la primera de las validas
        return valid[0]        