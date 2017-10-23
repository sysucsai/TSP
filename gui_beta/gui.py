#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import random
import matplotlib
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.n = 0

        self.initUI()
    #@QtCore.pyqtSlot(int)
    def change(self):

        self.n += 1
        msgBox=QMessageBox.about(self, "test", "clicked " + str(self.n))
        print('ok clicked '+ str(self.n))
        pass

    def output(self):
        return self.n


    def initUI(self):
        self.btn = QPushButton("start", self)
        self.btn.clicked.connect(self.change)
        #self.connect(btn,QtCore.SIGNAL('clicked()'),self.change)
        #btn.clicked.connect(change)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(500, 500)

        self.setGeometry(100, 200, 1080, 720)
        self.setWindowTitle('Tooltips')
        self.ls_btn = QRadioButton("local search")
        self.sa_btn = QRadioButton("simulated annealing")

        self.ls_btn.move(400, 400)
        self.sa_btn.move(400, 500)

        #self._xpButton.toggled.connect(lambda:self.changeStyle("WindowsXP"))
        #self._windowSButton.toggled.connect(lambda:self.changeStyle("Windows"))

        layout = QVBoxLayout()
        layout.addWidget(self.ls_btn)
        layout.addWidget(self.sa_btn)
        layout.addStretch(1)

        self.setLayout(layout)

    #def changeStyle(self,styleName):
        #QApplication.setStyle(QStyleFactory.create(styleName))




if __name__ == '__main__':



    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
