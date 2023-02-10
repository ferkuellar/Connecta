import pyfiglet

class Game():
    
    def start(self):
        # imprimo el nombre o logo del juego
        self.print_logo()
        # configuro la partida
        # arranco el game loop

    def print_logo(self):
        logo = pyfiglet.Figlet(font = 'stop')
        print(logo.renderText('Connecta'))
