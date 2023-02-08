from list_utils import find_streak
from settings import BOARD_LENGTH, VICTORY_STRIKE

class LinearBoard():
    # CLASE QUE REPRESENTA UN TABLERO DE U NA SOLA COLUMNA 
    # X UN JUGADOR 
    # O OTRO JUGADOR
    # None UN ESPACIO VACIO

    @classmethod
    def fromList(cls, list):
        board = cls()
        board._column = list
        return board
    
    def __init__(self):
    # UNA LISTA DE None
        
        self._column =[None for i in range(BOARD_LENGTH)]

    def add(self, char):
    # JUEGA EN LA PRIMERA POSICION DESIPONIBLE
    
        #SIEMPRE Y CUANDO NO ESTE LLENO ......
        if not self.is_full():
            #BUSCAMOS LA PRIMERA POSISCION DISPONIBLE(None)
            i = self._column.index(None)
            #LO SUSTIUIMIOS POR CAHR
            self._column[i] = char


    def is_full(self):
        return self._column[-1] != None

    def is_victory(self, char):
        return find_streak(self._column, char, VICTORY_STRIKE)
    
    def is_tie(self, char1, char2):
        # NO HAY VISTORIA NI CHAR1 NI DE CHAR2
        return (self.is_victory('x') == False) and (self.is_victory('o') == False)
