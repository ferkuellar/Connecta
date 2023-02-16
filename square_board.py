from linear_board import LinearBoard
from list_utils import transpose, displace_matrix, reverse_matrix, collapse_matrix, replace_all_in_matrix
from settings import BOARD_LENGTH
from string_utils import explode_list_of_strings


class SquareBoard():
    # Representa un tablero cuadrado

    @classmethod
    def fromList(cls, list_of_lists):
        #Transforma una lista de lista en un lista de linearBoard
        board = cls()
        board._columns = list(map(lambda element: LinearBoard.fromList(element), list_of_lists))
        return board

    @classmethod
    def fromBoardCode(cls, board_code):
        return cls.fromBoardRawCode(board_code.raw_code)
    
    @classmethod
    def fromBoardRawCode(cls, board_raw_code):
        # transforma la cadena en fromato de BoardCode en una lista de LinearBoard y luego lo transforma en un tablero cuadrado

        # 1. convertir la cedena del codigo de una lista de cadenas
        list_of_strings = board_raw_code.split("|")

        # 2. transformar cada cadena en una lista de caracteres
        matrix = explode_list_of_strings(list_of_strings)

        # 3. cambiamos todas las ocurrencias de . por none
        matrix = replace_all_in_matrix(matrix, '.', None)
        
        # 4. transformamos esa lista en un SquareBoard
        return cls.fromList(matrix)

    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)]

    def __repr__(self):
        return f'{self.__class__}: {self._columns}'
    
    def __len__(self):
        return len(self._columns)
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._columns == other._columns
    
    def __hash__(self):
        return hash(self._columns)

    def is_full(self):
        # True si todos los LinearBoard estan llenos

        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result
    
    def as_code(self):
        return BoardCode(self)
    
    def as_matrix(self):
        #devuelve una represenatcion en formato matiz es decir lista de listas
        return list(map(lambda x: x._column, self._columns))
    
        # juega una ficha
    def add(self, char, column):
        self._columns[column].add(char)
    
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
        m = self.as_matrix()
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
    
class BoardCode:

    def __init__(self, board):
        self._raw_code = collapse_matrix(board.as_matrix())

    @property
    def raw_code(self):
        return self._raw_code
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            # solo importa el raw code
            return self.raw_code == other.raw_code
    
    def __hash__(self):
        return hash(self.raw_code)
    
    def __repr__(self):
        return f'{self.__class__} : {self.raw_code}'
