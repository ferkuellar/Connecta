class Match():

    def __init__(self, player1, player2):
        player1.char = 'x'
        player2.char = 'o'
        player1.opponent = player2

        self._players = {'x' : player1, 'o': player2}
        self._round_robbin = [player1, player2]

    @property
    def next_player(self):
        next = self._round_robbin[0]
        self._round_robbin.reverse()
        return next
    
    def get_player(self, char):
        return self._players[char]
    
    def get_winner(self, board):
        # devuelve el jugador ganador y si no lo hay, devuelve none
        if board.is_victory('x'):
            return self.get_player('x')
        elif board.is_victory('o'):
            return self.get_player('o')
        else:
            return None
        
    def is_match_over(self):
        # pregunta al usuario si gusta otra partida
        result = True
        while True:
            answer = input('Would you like to play another match? (Y/N): ').upper()
            if answer == 'Y':
                result = False
                break
            elif answer == 'N':
                result = True
                break
        return result
