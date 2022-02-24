from PyQt5 import QtCore, QtGui, QtWidgets
from DP832_iontrap1_gui import Ui_Form


class DP832_iontrap1_control_window(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(DP832_iontrap1_control_window, self).__init__()
        self.setupUi(self)  
