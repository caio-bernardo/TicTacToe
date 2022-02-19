""" window module: responsible for the front actions of the Game. """
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from ..interface.uic.game_gui import Ui_MainWindow
from . import tools


class Window(QMainWindow, Ui_MainWindow):
    """Initialize the UI and set buttons functions and labels texts."""
    VERSION = '1.0.0-rc0'
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        DEFAULT_PAGE = self.start_page
        self.stackedWidget.setCurrentWidget(DEFAULT_PAGE)

        # Bottom Label
        self.bottom_label.setText(f'v-{self.VERSION}')

        # Start Page - Default
        self.btn_1p.clicked.connect(self.go_to_board_page_n_singleplayer)
        self.btn_2p.clicked.connect(self.go_to_board_page_n_twoplayer)
        self.btn_exit.clicked.connect(self.close)

        # Board Page
        self.grid_buttons: list[Ui_MainWindow] = (self.btn_grid1, self.btn_grid2, self.btn_grid3,
                                                  self.btn_grid4,self.btn_grid5, self.btn_grid6,
                                                  self.btn_grid7, self.btn_grid8, self.btn_grid9)
        
        # TODO Fix: os sinais dos botoes se confundem num loop, e o ultimo btn recebe sinais de todos os outros.
        self.btn_grid1.clicked.connect(lambda: self.run_a_turn(self.btn_grid1))
        self.btn_grid2.clicked.connect(lambda: self.run_a_turn(self.btn_grid2))
        self.btn_grid3.clicked.connect(lambda: self.run_a_turn(self.btn_grid3))
        self.btn_grid4.clicked.connect(lambda: self.run_a_turn(self.btn_grid4))
        self.btn_grid5.clicked.connect(lambda: self.run_a_turn(self.btn_grid5))
        self.btn_grid6.clicked.connect(lambda: self.run_a_turn(self.btn_grid6))
        self.btn_grid7.clicked.connect(lambda: self.run_a_turn(self.btn_grid7))
        self.btn_grid8.clicked.connect(lambda: self.run_a_turn(self.btn_grid8))
        self.btn_grid9.clicked.connect(lambda: self.run_a_turn(self.btn_grid9))

        # Result Page
        self.btn_return_2_main.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.start_page)
            )

    def go_to_board_page(self):
        """Clean the grid set the players and change the stackedWidget to board_page.
        """
        for btn in self.grid_buttons:
            btn.setText('')

        self.brd = tools.Board()

        self.player = tools.Player()
        self.crrnt_ply_label.setText(self.player.nowply['name'])


        self.stackedWidget.setCurrentWidget(self.board_page)
    
    def go_to_board_page_n_singleplayer(self):
        """Set the game mode to Single Player go to board_page."""
        self.go_to_board_page()
        self.game_mode = tools.GameMode.SINGLEMODE
    
    def go_to_board_page_n_twoplayer(self):
        """Set the game mode to Two Player go to board_page."""
        self.go_to_board_page()
        self.game_mode = tools.GameMode.TWOMODE

    def run_a_turn(self, btn: Ui_MainWindow) -> None:
        """Starts a turn in the game executes different methods and end the turn.

        It tries to write on the grid, check if the game is finished and
         changes the current player, ending the turn.
        
        If its in the Single Player Mode, it also runs the computer turn.

        Args:
            btn (Ui_MainWindow): button clicked by the player
        """
        sign = self.player.nowply['sign']
        
        if self.game_mode == tools.GameMode.SINGLEMODE:
            if self.player_move(btn, sign) is False:
                return
            
            if self.has_game_finnished() is True:
                return

            self.change_player()

            if self.computer_move(self.player.nowply['sign']) is True:
                
                if self.has_game_finnished() is True:
                    return
                
                self.change_player()
        
        elif self.game_mode == tools.GameMode.TWOMODE:
            if self.player_move(btn, sign) is False:
                return
            
            if self.has_game_finnished() is True:
                return

            self.change_player()
        
    def has_game_finnished(self):
        """Check if the game is finished using GameState class."""

        # With game_state here it always receives the current player and doens't stay outdated.
        self.game_state = tools.GameState(player=self.player.nowply, board=self.brd)
        final_result = self.game_state.check_state()
        
        if not final_result is None:
            msg, img = final_result
            
            self.result_label.setText(msg)
            self.result_img_label.setPixmap(QtGui.QPixmap(img))
            self.stackedWidget.setCurrentWidget(self.result_page)
            
            return True
    
    def change_player(self):
        """ Change Player."""
        self.player.swap()
        self.crrnt_ply_label.setText(self.player.nowply['name'])

    def computer_move(self, sign: str):
        """Choose and try to change a button text to its symbol.

        Args:
            sign (str): symbol to be put on the button

        Returns:
            bool: returns if it has success on the action
        """
        cmd = tools.ComputerMove(self.brd)
        location = cmd.choose_location()
        if location is None:
            return

        btn = self.grid_buttons[location]

        if self.brd.write_on(location + 1, sign) is True:
            btn.setText(sign)      
            return True
        else:
            return False 

    def player_move(self,btn: Ui_MainWindow, sign: str) -> bool:
        """Tries to change the button text to the players symbol.

        Args:
            btn (Ui_MainWindow): the button that was clicked
            sign (str): symbol to be put on the button

        Returns:
            bool: returns if it has success on the action
        """
        btn_name: str = btn.objectName()
        dit = int(btn_name[-1])
        
        if self.brd.write_on(dit, sign) is True:
            btn.setText(sign)
            return True
        else:
            return False
