from functools import partial
from time import sleep
from PyQt5.QtWidgets import QMainWindow
from game import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.go_to_board_page = partial(self.stackedWidget.setCurrentWidget, self.board_page)
        self.go_to_main_page = partial(self.stackedWidget.setCurrentWidget, self.start_page)
        
        # Main Page
        self.btn_1p.clicked.connect(self.go_to_board_page)
        self.btn_2p.clicked.connect(self.go_to_board_page)
        self.btn_exit.clicked.connect(self.close)

        # Board Page
        self.board = ["" for _ in range(9)]
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
        self.commandLinkButton.clicked.connect(self.)
        
    def write_on_board(self, btn: Ui_MainWindow):
        if not btn.text() == '':
            return
        
        sign = self.get_current_plyr()
        btn.setText(sign)

        btn_name: str = btn.objectName()
        dit = int(btn_name[-1])
        self.board[dit -1] = sign


        # Check winner
        self.check_result()

        self.set_current_player()

    def get_current_plyr(self, getname:bool=False):
        current_plyr = self.crrnt_ply_label.text()
        if current_plyr == 'Player 1':
            return current_plyr if getname is True else 'X'
        elif current_plyr == 'Player 2':
            return current_plyr if getname is True else 'O' 

    def set_current_player(self):
        old_player = self.get_current_plyr(getname=True)
        if old_player == 'Player 1':
            self.crrnt_ply_label.setText('Player 2')
        elif old_player == 'Player 2':
            self.crrnt_ply_label.setText('Player 1')

    def check_result(self):
        if self.winner():
            sleep(0.2)
            

        elif all([c != "" for c in self.board]):
            sleep(0.2)
            print('Tie game')    


    def winner(self):
        s = self.get_current_plyr()
        b = self.board
        return ((b[0] == b[1] == b[2] == s) or
                (b[3] == b[4] == b[5] == s) or
                (b[6] == b[7] == b[8] == s) or
                (b[0] == b[3] == b[6] == s) or
                (b[1] == b[4] == b[7] == s) or
                (b[2] == b[5] == b[8] == s) or
                (b[0] == b[4] == b[8] == s) or
                (b[2] == b[4] == b[6] == s)
                )