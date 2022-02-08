"""
Run this to test the application

"""
from .src import window
import sys
from PyQt5.QtWidgets import QApplication

def start():
    qt = QApplication(sys.argv)
    win = window.Window()
    win.show()
    qt.exec_()

