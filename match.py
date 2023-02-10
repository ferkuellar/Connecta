class Match():

    def __ini__(self, player1, player2):
        player1.char = 'x'
        player2.char = 'o'
        player1.opponent = player2

        self._players = {'x' : player1, 'o': player2}
        