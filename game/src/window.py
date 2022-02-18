
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from ..interface.uic.game_gui import Ui_MainWindow
from . import tools


class Window(QMainWindow, Ui_MainWindow):
    VERSION = '0.3.0'
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
        self.btn_grid1.clicked.connect(lambda: self.write_on_board(self.btn_grid1))
        self.btn_grid2.clicked.connect(lambda: self.write_on_board(self.btn_grid2))
        self.btn_grid3.clicked.connect(lambda: self.write_on_board(self.btn_grid3))
        self.btn_grid4.clicked.connect(lambda: self.write_on_board(self.btn_grid4))
        self.btn_grid5.clicked.connect(lambda: self.write_on_board(self.btn_grid5))
        self.btn_grid6.clicked.connect(lambda: self.write_on_board(self.btn_grid6))
        self.btn_grid7.clicked.connect(lambda: self.write_on_board(self.btn_grid7))
        self.btn_grid8.clicked.connect(lambda: self.write_on_board(self.btn_grid8))
        self.btn_grid9.clicked.connect(lambda: self.write_on_board(self.btn_grid9))

        # Result Page
        self.btn_return_2_main.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.start_page)
            )

    def go_to_board_page(self):
        for btn in self.grid_buttons:
            btn.setText('')

        self.brd = tools.Board()

        self.player = tools.Player()
        self.crrnt_ply_label.setText(self.player.nowply['name'])

        self.game_state = tools.GameState(player=self.player.nowply, board=self.brd)

        self.stackedWidget.setCurrentWidget(self.board_page)
    
    def go_to_board_page_n_singleplayer(self):
        self.go_to_board_page()
        self.game_mode = 'Single Player'
    
    def go_to_board_page_n_twoplayer(self):
        self.go_to_board_page()
        self.game_mode = 'Two Players'

    def write_on_board(self, btn: Ui_MainWindow) -> None:
        sign = self.player.nowply['sign']

        btn_name: str = btn.objectName()
        dit = int(btn_name[-1])
        
        if self.brd.write_on(dit, sign) is True:
            btn.setText(sign)
        else:
            return        

        # Check if the game is finished
        # TODO Fix GameState not updating player
        self.game_state.player = self.player.nowply

        final_result = self.game_state.check_state()
        
        if not final_result is None:
            msg, img = final_result
            
            self.result_label.setText(msg)
            self.result_img_label.setPixmap(QtGui.QPixmap(img))
            self.stackedWidget.setCurrentWidget(self.result_page)
            
            return
        
        # Change Player
        self.player.swap()
        self.crrnt_ply_label.setText(self.player.nowply['name'])

        if self.game_mode == 'Single Player':
            self.computer_move()

    def computer_move(self):
        sign = self.player.nowply['sign']

        cmd = tools.ComputerMove(self.brd)
        location = cmd.choose_location()
        if location is None:
            return

        btn = self.grid_buttons[location]

        if self.brd.write_on(location + 1, sign) is True:
            btn.setText(sign)
        else:
            return        

        # Check if the game is finished
        # TODO Fix GameState not updating player
        self.game_state.player = self.player.nowply

        final_result = self.game_state.check_state()
        
        if not final_result is None:
            msg, img = final_result
            
            self.result_label.setText(msg)
            self.result_img_label.setPixmap(QtGui.QPixmap(img))
            self.stackedWidget.setCurrentWidget(self.result_page)
            
            return
        
        # Change Player
        self.player.swap()
        self.crrnt_ply_label.setText(self.player.nowply['name'])