from MARTHAui import Ui_MARTHA_UI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime, QTimer, QDate
from PyQt5.uic import loadUiType
import main
import sys

class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__

    def run(self):
        main.Task_Gui()

startExe = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__

        self.gui = Ui_MARTHA_UI
        self.gui.setupUi(self)

        self.gui.Pushbutton_start.clicked.connect(self.startTask)
        self.gui.Pushbutton_exit.clicked.connect(self.close)

    def startTask(self):
        
        self.gui.label1 = QtGui.QMovie("MARTHA GUI MATERIALS//faceman.gif")
        self.gui.GIF1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("MARTHA GUI MATERIALS//spheres-motion-for-ai-product-design-by-gleb-large.gif")
        self.gui.GIF3.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("GUI For MARTHA//B.G_Template_1.gif")
        self.gui.GIF6_2.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("MARTHA GUI MATERIALS//9e759fd37ccd98da121b670249f34afa.gif")
        self.gui.GIF4.setMovie(self.gui.label4)
        self.gui.label4.start()
        
        self.gui.label5 = QtGui.QMovie("MARTHA GUI MATERIALS//T8bahf.gif")
        self.gui.GIF5.setMovie(self.gui.label5)
        self.gui.label5.start()

        self.gui.label6 = QtGui.QMovie("GUI For MARTHA//Earth_Template.gif")
        self.gui.label_2.setMovie(self.gui.label6)
        self.gui.label6.start()

        startExe.start()

GuiApp = QApplication(sys.argv)
Martha_gui = Gui_Start()
Martha_gui.show()
exit(GuiApp.exec_())


