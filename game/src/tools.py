from random import choice
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
    
    def swap(self):
        self._nowply, self._oldply = self._oldply, self._nowply
    
    def reset(self):
        self._nowply = {'name': 'Player 1', 'sign': 'X'}
        self._oldply = {'name': 'Player 2', 'sign': 'O'}


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
        self.checkwinner = CheckWinner()

    def check_state(self) -> Union[tuple, None]:
        winner = self.checkwinner.check_4_winner(self.player['sign'], self.board.board)
        if winner is True:
           player_name: str = self.player['name'] 
           self.options[player_name]()
           return self.results.return_results() 
        
        elif self.board.is_board_full():
            self.options['Tie Game']()
            return self.results.return_results() 
        
        else:
            return None

class CheckWinner:
    def check_4_winner(self, s: str, b: list) -> bool:
        return ((b[0] == b[1] == b[2] == s) or
                (b[3] == b[4] == b[5] == s) or
                (b[6] == b[7] == b[8] == s) or
                (b[0] == b[3] == b[6] == s) or
                (b[1] == b[4] == b[7] == s) or
                (b[2] == b[5] == b[8] == s) or
                (b[0] == b[4] == b[8] == s) or
                (b[2] == b[4] == b[6] == s))

class ComputerMove:
    def __init__(self, brd: Board):
        self.brd = brd.board
        self.available_locations = [k for k, v in enumerate(self.brd) if v == '']
        self.checkwinner = CheckWinner()
    
    def choose_location(self):
        options_2_pick = (self.win_or_ruin, self.pick_corner, self.pick_center,
                          self.pick_edge, self.pick_random)
        location = None
        for option in options_2_pick:
            location = option()
            if location:
                break

        return location

    def win_or_ruin(self):
        for s in ('X','O'):
            for l in self.available_locations:
                copy_board = self.brd[:]
                copy_board[l] = s
                if self.checkwinner.check_4_winner(s, copy_board) is True:
                    return l

    def pick_corner(self):
        options = tuple(filter(lambda n: n in [0, 2, 6, 8], self.available_locations))
        if options: 
            return choice(options)

    def pick_center(self):
        if 4 in self.available_locations:
            return 4

    def pick_edge(self):
        options = tuple(filter(lambda n: n in [1, 3, 5, 7], self.available_locations))
        if options: 
            return choice(options)

    def pick_random(self):
        if self.available_locations:
            return choice(self.available_locations)
