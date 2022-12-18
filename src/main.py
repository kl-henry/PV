#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
import sys
from src.mainwindow import  Ui_MainWindow
from PySide2 import QtWidgets

if __name__ == "__main__":
    app =QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.setupUi(window)
    window.show()
    sys.exit(app.exec_())
