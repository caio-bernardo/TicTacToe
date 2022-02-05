from interface import *
import sys
from PyQt5.QtWidgets import QApplication

def main():
    qt = QApplication(sys.argv)
    win = Window()
    win.show()
    qt.exec_()

if __name__ == "__main__":
    main()