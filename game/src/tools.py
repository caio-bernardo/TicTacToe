from typing import Union


class Board:
    def __init__(self):
        self.board = ['' for _ in range(9)]

    def is_location_free(self, location) -> bool:
        if self.board[location - 1] == '':
            return True
        return False

    def is_board_full(self) -> bool:
        return all([c != '' for c in self.board])

    def write_on(self, location, sign) -> bool:
        if not self.is_location_free(location):
            return False

        self.board[location - 1] = sign
        return True


class Player:
    """ A class that swap between the two players using getter and setters."""
    def __init__(self):
        self._nowply = {'name': 'Player 1', 'sign': 'X'}
        self._oldply = {'name': 'Player 2', 'sign': 'O'}
    
    @property
    def nowply(self):
        return self._nowply

    @nowply.setter
    def nowply(self, value):  # TODO remove this setter (swap does the job now)
        """ value it's a flag for the swap """
        if value != '':
            self._nowply, self._oldply = self._oldply, self._nowply
    
    def swap(self):
        self.nowply = 'swap'
    
    def reset(self):
        self._nowply = {'name': 'Player 1', 'sign': 'X'}
        self._oldply = {'name': 'Player 2', 'sign': 'O'}


class Button:
    pass


class Results():
    def __init__(self):
        self.mensage = 'Default'
        self.image_resource = 'None'

    def ply1_wins(self):
        self.mensage = 'Player 1!'
        self.image_resource = ':/resources/cross_symbol.png'
    
    def ply2_wins(self):
        self.mensage = 'Player 2!'
        self.image_resource = ':/resources/circle_symbol.png'

    def no_wins(self):
        self.mensage = 'Tie Game!'
        self.image_resource = ':/resources/tie_game.png'

    def return_results(self) -> tuple:
        return (self.mensage, self.image_resource)


class GameState:
    def __init__(self, player: Player, board: Board):
        self.results = Results()
        self.options = {'Player 1': self.results.ply1_wins,
         'Player 2': self.results.ply2_wins, 'Tie Game': self.results.no_wins}
        self.player = player
        self.board = board

    def check_state(self) -> Union[tuple, None]:
        winner = self.__check_4_winner()
        if winner is True:
           player_name: str = self.player['name'] 
           self.options[player_name]()
           return self.results.return_results() 
        
        elif self.board.is_board_full():
            self.options['Tie Game']()
            return self.results.return_results() 
        
        else:
            return None

    def __check_4_winner(self) -> bool:
        s = self.player['sign']
        b = self.board.board

        return ((b[0] == b[1] == b[2] == s) or
                (b[3] == b[4] == b[5] == s) or
                (b[6] == b[7] == b[8] == s) or
                (b[0] == b[3] == b[6] == s) or
                (b[1] == b[4] == b[7] == s) or
                (b[2] == b[5] == b[8] == s) or
                (b[0] == b[4] == b[8] == s) or
                (b[2] == b[4] == b[6] == s))
