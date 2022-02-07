from unittest import result
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from interface.uic.game_gui import Ui_MainWindow
from src import tools

class Window(QMainWindow, Ui_MainWindow):
    VERSION = '0.1.0'
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        DEFAULT_PAGE = self.start_page
        self.stackedWidget.setCurrentWidget(DEFAULT_PAGE)

        # Bottom Label
        self.bottom_label.setText(f'v-{self.VERSION}')

        # Start Page - Default
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
        self.btn_grid1.setText('')
        self.btn_grid2.setText('')
        self.btn_grid3.setText('')
        self.btn_grid4.setText('')
        self.btn_grid5.setText('')
        self.btn_grid6.setText('')
        self.btn_grid7.setText('')
        self.btn_grid8.setText('')
        self.btn_grid9.setText('')

        self.brd = tools.Board()

        self.player = tools.Player()
        self.crrnt_ply_label.setText(self.player.nowply['name'])

        self.stackedWidget.setCurrentWidget(self.board_page)
        
    def write_on_board(self, btn: Ui_MainWindow) -> None:
        sign = self.player.nowply['sign']

        btn_name: str = btn.objectName()
        dit = int(btn_name[-1])
        
        if self.brd.write_on(dit, sign) is True:
            btn.setText(sign)
        else:
            return        

        # Check winner
        is_finished = self.check_result()
        
        if is_finished is True:
            self.result_label.setText(self.resul.mensage)
            self.result_img_label.setPixmap(QtGui.QPixmap(self.resul.image_resource))
            self.stackedWidget.setCurrentWidget(self.result_page)
            return
        
        # Change Player
        self.player.nowply = 'swap'
        self.crrnt_ply_label.setText(self.player.nowply['name'])

    def check_result(self) -> bool:
        self.resul = tools.Results()
        if tools.check_4_winner():
            if self.player.nowply['name'] == 'Player 1':
                self.resul.ply1_wins()
            else:
                self.resul.ply2_wins()

            return True
        
        elif self.brd.is_board_full():
            self.resul.no_wins()
            return True
        
        return False
