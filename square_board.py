from linear_board import LinearBoard
from list_utils import transpose, displace_matrix, reverse_matrix
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
    
    def as_matrix(self):
        #devuelve una represenatcion en formato matiz es decir lista de listas
        return list(map(lambda x: x._column, self._columns))

    
    # Detetctar victoria
    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)
    
    def _any_vertical_victory(self, char):
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result
    
    def _any_horizontal_victory(self, char):
        # Transponemos _columns
        transp = transpose(self.as_matrix())
        # Creamos un tablero temporal con esa matriz transpuesta
        tmp = SquareBoard.fromList(transp)

        # comprobamos si tiene una victoria temporal
        return tmp._any_vertical_victory(char)
        
    
    def _any_rising_victory(self, char):
        # Obtener las columnas
        m = self.as_matrix
        # Las invertimos
        rm = reverse_matrix(m)
        # Creamos tablero temporal con esa matriz
        tmp = SquareBoard.fromList(rm)
        # Devolvemos si tiene una victoria descendente
        return tmp._any_sinking_victory(char)
    
    def _any_sinking_victory(self, char):
        # Obtenemos las columnas como una mariz
        m = self.as_matrix()
        # Las despalzamos al final
        d = displace_matrix(m)
        # Creamos un tablero temporal con esa matriz
        tmp = SquareBoard.fromList(d)
        # Averiguamos si tiene una victoria horizontal
        return tmp._any_horizontal_victory(char)
    

    # Dunders metodos magicos para hacer clases

    def __repr__(self):
        return f'{self.__class__}:{self._columns}'
