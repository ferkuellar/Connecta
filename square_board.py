from linear_board import LinearBoard
from settings import BOARD_LENGTH


class SquareBoard():
    # Representa un tablero cuadrado

    @classmethod
    def fromList(cls, list_of_lists):
        #Transforma una lista de lista en un lista de linearBoard
        board = cls()
        board._columns = list(map(lambda element: LinearBoard.fromList(element), list_of_lists))
        return board

    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)]

    def is_full(self):
        # True si todos los LinearBoard estan llenos

        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result
    
    # Detetctar victoria
    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)
    
    def _any_vertical_victory(self, char):
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result
    
    def _any_horizontal_victory(self, cahr):
        return False
    
    def _any_rising_victory(self, char):
        return False
    
    def _any_sinking_victory(self, char):
        return False
    
    # Dunders metodos magicos para hacer clases

    def __repr__(self):
        return f'{self.__class__}:{self._columns}'
