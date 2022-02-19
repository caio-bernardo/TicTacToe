"""
The tools module: responsible for different backgorund actions on the Game. 
"""
from enum import Enum, auto
from random import choice
from typing import Union


class GameMode(Enum):
    """An Enum for the gamemode types."""
    SINGLEMODE = auto()
    TWOMODE = auto()


class Board:
    """Creates a 3x3 grid as a list and interact with it.
    """
    def __init__(self):
        self.board = ['' for _ in range(9)]

    def is_location_free(self, location: int) -> bool:
        """Check if the location param on the grid is an empty string.

        Args:
            location (int): an index number of the 3x3 grid, should be (1-9).

        Returns:
            bool: returns with the index location is an empty string.
        """
        if self.board[location - 1] == '':
            return True
        return False

    def is_board_full(self) -> bool:
        """Checks if the at least on of the slots of 3x3 grid has and empty string.

        Returns:
            bool: return a booleand depending if there are no empty strings on the grid.
        """
        return all([c != '' for c in self.board])

    def write_on(self, location: int, sign: str) -> bool:
        """Write the sign param on the location slot of the grid if available.

        Args:
            location (int): the index for the grid slot.
            sign (string): the symbol to be put on the grid slot.

        Returns:
            bool: returns if the action was a sucess or failed.
        """
        if not self.is_location_free(location):
            return False

        self.board[location - 1] = sign
        return True


class Player:
    """Defines and switch between the two players"""
    def __init__(self):
        """Defines the old player and the current player and their respective info."""
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


class Results:
    """ The class defines and return the values to be show on the result screen.
    
    The class set the mensage of the result (Tie Game|Player 1|Player 2) and 
     the image to be show on the screen.
    """
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
    """Check if the game has come to an end.

    It checks if one of the player has won or with the game is tied, if one of 
     this cases are True it returns info to set up the result page.
    """
    def __init__(self, player: Player, board: Board):
        self.results = Results()
        self.options = {'Player 1': self.results.ply1_wins,
         'Player 2': self.results.ply2_wins, 'Tie Game': self.results.no_wins}
        self.player = player
        self.board = board
        self.checkwinner = CheckWinner()

    def check_state(self) -> Union[tuple, None]:
        """Checks for winners or if it's a tie game returning None or the results.

        Returns:
            Union[tuple, None]: Info to be display on the result page.
        """
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
    """ Check for winner patterns on a grid.
    method:
        check_4_winner: Check if there's a winner pattern on the grid.
    """
    def check_4_winner(self, s: str, b: list) -> bool:
        """Check if there's a winner pattern on the grid.

        It goes through all combinations to win the game and see with the
         symbols on that slots are all igual to the s param. Thus, determining
         if a player wins the game.

        Args:
            s (str): the symbol to search on the grid
            b (list): the grid itself

        Returns:
            bool: returns if it has found a winner combination.
        """
        return ((b[0] == b[1] == b[2] == s) or
                (b[3] == b[4] == b[5] == s) or
                (b[6] == b[7] == b[8] == s) or
                (b[0] == b[3] == b[6] == s) or
                (b[1] == b[4] == b[7] == s) or
                (b[2] == b[5] == b[8] == s) or
                (b[0] == b[4] == b[8] == s) or
                (b[2] == b[4] == b[6] == s))


class ComputerMove:
    """Takes the available slots on the 3x3 grid and strategicaly choose a slot."""
    def __init__(self, brd: Board):
        self.brd = brd.board
        self.available_locations = [k for k, v in enumerate(self.brd) if v == '']
        self.checkwinner = CheckWinner()
    
    def choose_location(self) -> int:
        """It goes through all options to choose a location until it finds a valid slot.

        Returns:
            int: returns the choosen location
        """
        options_2_pick = (self.win_or_ruin, self.pick_corner, self.pick_center,
                          self.pick_edge, self.pick_random)
        location = None
        
        for option in options_2_pick:
            location = option()
            if location:
                break

        return location

    def win_or_ruin(self) -> int:
        """Check if its possible for one of the player wins and returns a
            location to win or ruin a win for a player.
        
        It checks using the 2 symbols (X, O) and CheckWinner class, if filling 1
         of the available slots will make a player win. If yes, it returns that
         position.

        Returns:
            int: the choosen slot on the grid
        """
        for s in ('O','X'):
            for l in self.available_locations:
                copy_board = self.brd[:]
                copy_board[l] = s
                if self.checkwinner.check_4_winner(s, copy_board) is True:
                    return l

    def pick_corner(self) -> int:
        """If possible, choose randomly one of the corner slots of the grid.

        It filters from the available locations the corner slots and selects one.

        Returns:
            int: the choosen slot of the grid
        """
        options = tuple(filter(lambda n: n in [0, 2, 6, 8], self.available_locations))
        if options: 
            return choice(options)

    def pick_center(self) -> int:
        """ If the center slot is available returns it."""
        if 4 in self.available_locations:
            return 4

    def pick_edge(self):
        """If possible, choose randomly one of the edge slots of the grid.

        It filters from the available locations the edge slots and selects one.

        Returns:
            int: the choosen slot of the grid
        """
        options = tuple(filter(lambda n: n in [1, 3, 5, 7], self.available_locations))
        if options: 
            return choice(options)

    def pick_random(self):
        """It choose randomly an available location.
        """
        if self.available_locations:
            return choice(self.available_locations)
