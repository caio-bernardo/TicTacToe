"""
Run this to test the application

"""
from src.main import Window
import sys
from PyQt5.QtWidgets import QApplication

def start():
    qt = QApplication(sys.argv)
    win = Window()
    win.show()
    qt.exec_()


if __name__ == "__main__":
    start()
