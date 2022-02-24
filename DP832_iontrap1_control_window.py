from PyQt5 import QtCore, QtGui, QtWidgets
from DP832_iontrap1_gui_import import DP832_iontrap1_control_window
import sys
from DP832_iontrap1 import DP832_Flip, DP832_Oven_PMT

class DP832_control(DP832_iontrap1_control_window):
    def __init__(self):
        super().__init__()
        self.PSU_Flip = DP832_Flip()
        self.Flip_CH2_ON.clicked.connect(lambda:self.Flip_CH2_output_on())
        self.Flip_CH2_OFF.clicked.connect(lambda:self.Flip_CH2_output_off())
        
        self.PSU_Oven_PMT = DP832_Oven_PMT()
        self.Oven_CH1_ON.clicked.connect(lambda:self.Oven_CH1_output_on())
        self.Oven_CH1_OFF.clicked.connect(lambda:self.Oven_CH1_output_off())
        self.Oven_CH2_ON.clicked.connect(lambda:self.Oven_CH2_output_on())
        self.Oven_CH2_OFF.clicked.connect(lambda:self.Oven_CH2_output_off())
        self.PMT_CH3_ON.clicked.connect(lambda:self.PMT_CH3_output_on())
        self.PMT_CH3_OFF.clicked.connect(lambda:self.PMT_CH3_output_off())

    def Flip_CH2_output_on(self):
        self.PSU_Flip.toggle_output(2, 1)
        self.Flip_CH2_state.setText('ON')
    
    def Flip_CH2_output_off(self):
        self.PSU_Flip.toggle_output(2, 0)
        self.Flip_CH2_state.setText('OFF')
    
    def Oven_CH1_output_on(self):
        self.PSU_Oven_PMT.toggle_output(1, 1)
        self.Oven_CH1_state.setText('ON')
    
    def Oven_CH1_output_off(self):
        self.PSU_Oven_PMT.toggle_output(1, 0)
        self.Oven_CH1_state.setText('OFF')
        
    def Oven_CH2_output_on(self):
        self.PSU_Oven_PMT.toggle_output(2, 1)
        self.Oven_CH2_state.setText('ON')
    
    def Oven_CH2_output_off(self):
        self.PSU_Oven_PMT.toggle_output(2, 0)
        self.Oven_CH2_state.setText('OFF')
        
    def PMT_CH3_output_on(self):
        self.PSU_Oven_PMT.toggle_output(3, 1)
        self.PMT_CH3_state.setText('ON')
    
    def PMT_CH3_output_off(self):
        self.PSU_Oven_PMT.toggle_output(3, 0)
        self.PMT_CH3_state.setText('OFF')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = DP832_control()
    a.show()
    sys.exit(app.exec_())