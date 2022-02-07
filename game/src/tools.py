

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
    def nowply(self, value):
        """ value it's a flag for the swap """
        if value != '':
            self._nowply, self._oldply = self._oldply, self._nowply
    
    def reset(self):
        self._nowply = {'name': 'Player 1', 'sign': 'X'}
        self._oldply = {'name': 'Player 2', 'sign': 'O'}


class Results():
    def __init__(self):
        self._mensage = 'Default'
        self._image_resource = 'None'

    @property
    def mensage(self):
        return self._mensage
    
    @mensage.setter
    def mensage(self, value):
        self._mensage = value
    
    @property
    def image_resource(self):
        return self._image_resource
    
    @image_resource.setter
    def image_resource(self, value):
        self._image_resource = value

    def ply1_wins(self):
        self.mensage = 'Player 1!'
        self.image_resource = ':/resources/cross_symbol.png'
    
    def ply2_wins(self):
        self.mensage = 'Player 2!'
        self.image_resource = ':/resources/circle_symbol.png'

    def no_wins(self):
        self.mensage = 'Tie Game!'
        self.image_resource = ':/resources/tie_game.png'


def check_4_winner(self, b, s) -> bool:
    return ((b[0] == b[1] == b[2] == s) or
            (b[3] == b[4] == b[5] == s) or
            (b[6] == b[7] == b[8] == s) or
            (b[0] == b[3] == b[6] == s) or
            (b[1] == b[4] == b[7] == s) or
            (b[2] == b[5] == b[8] == s) or
            (b[0] == b[4] == b[8] == s) or
            (b[2] == b[4] == b[6] == s))
