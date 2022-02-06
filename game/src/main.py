from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from interface.uic.game_gui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    VERSION = '0.1.0'

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # Bottom Label
        self.bottom_label.setText(f'v-{self.VERSION}')

        # Start Page - Default
        self.stackedWidget.setCurrentWidget(self.start_page)
        self.btn_1p.clicked.connect(self.go_to_board_page)
        self.btn_2p.clicked.connect(self.go_to_board_page)
        self.btn_exit.clicked.connect(self.close)

        # Board Page
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
        self.clean_board_page()
        self.stackedWidget.setCurrentWidget(self.board_page)

    def clean_board_page(self):
        self.board = ['' for _ in range(9)]
        self.btn_grid1.setText('')
        self.btn_grid2.setText('')
        self.btn_grid3.setText('')
        self.btn_grid4.setText('')
        self.btn_grid5.setText('')
        self.btn_grid6.setText('')
        self.btn_grid7.setText('')
        self.btn_grid8.setText('')
        self.btn_grid9.setText('')
        self.crrnt_ply_label.setText('Player 1')

    def write_on_board(self, btn: Ui_MainWindow) -> None:
        if not btn.text() == '':
            return

        sign = self.get_current_plyr()
        btn.setText(sign)

        btn_name: str = btn.objectName()
        dit = int(btn_name[-1])
        self.board[dit - 1] = sign

        # Check winner
        finished_game = self.check_result()
        if finished_game is False:
            # Change Player
            self.set_current_player()

    def get_current_plyr(self, getname: bool = False) -> str:
        current_plyr = self.crrnt_ply_label.text()
        if current_plyr == 'Player 1':
            return current_plyr if getname is True else 'X'
        elif current_plyr == 'Player 2':
            return current_plyr if getname is True else 'O'

    def set_current_player(self) -> None:
        old_player = self.get_current_plyr(getname=True)
        if old_player == 'Player 1':
            self.crrnt_ply_label.setText('Player 2')
        elif old_player == 'Player 2':
            self.crrnt_ply_label.setText('Player 1')

    def check_result(self) -> bool:

        if self.winner():
            if self.crrnt_ply_label.text() == 'Player 1':
                plyr_winner = 'Player 1'
                result_img = ':/resources/cross_symbol.png'
            else:
                plyr_winner = 'Player 2'
                result_img = ':/resources/circle_symbol.png'

            self.result_label.setText(f'{plyr_winner}!')

            self.result_img_label.setPixmap(QtGui.QPixmap(result_img))
            self.stackedWidget.setCurrentWidget(self.result_page)
            return True

        elif all([c != "" for c in self.board]):
            self.result_label.setText('Tie Game!')
            result_img = ':/resources/tie_game.png'
            self.result_img_label.setPixmap(QtGui.QPixmap(result_img))

            self.stackedWidget.setCurrentWidget(self.result_page)
            return True

        return False

    def winner(self) -> bool:
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
