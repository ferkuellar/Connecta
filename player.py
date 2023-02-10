from oracle import BaseOracle, ColumnClassification, ColumnRecommendation 


class Player():
    # juega en un tablero despues de preguntar al oraculo

    def __init__(self, name, char = None, oracle=BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle

    def play(self, board):
        # Elije la mejor columna de aquellas que recomienda el oraculo

        # Pregunto al oraculo () primeros es una tupla
        (best, recommendations) = self._ask_oracle(board)
        # Juego en la mejor
        self._play_on(board, best.index)

    def _play_on(self, board, postion):
        # juega en la posicion
        board.add(self.char, postion)

    def _ask_oracle(self, board):
        # pregunta al oraculo y devuelve la mejor opcion

        # obtenemos las recomendaciones
        recommendations = self._oracle.get_recommendation(board, self)
        # seleccionamos la mejor
        best = self._choose(recommendations)
        return(best, recommendations)



    def _choose(self, recomendations):
        # Quitamos la no validas
        valid = list(filter(lambda x : x.classification != ColumnClassification.FULL, recomendations))
        # Agarramos la primera de las validas
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
    