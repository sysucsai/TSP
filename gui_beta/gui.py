#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        self.btn = QPushButton(str(self.n), self)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.clicked.connect(self.change)
        #self.connect(btn,QtCore.SIGNAL('clicked()'),self.change)
        #btn.clicked.connect(change)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(500, 500)

        self.setGeometry(100, 200, 1080, 720)
        self.setWindowTitle('Tooltips')
        self._xpButton = QRadioButton("WindowsXP")
        self._windowSButton = QRadioButton("Windows")

        self._xpButton.toggled.connect(lambda:self.changeStyle("WindowsXP"))
        self._windowSButton.toggled.connect(lambda:self.changeStyle("Windows"))

        layout = QVBoxLayout()
        layout.addWidget(self._xpButton)
        layout.addWidget(self._windowSButton)
        layout.addStretch(1)

        self.setLayout(layout)

    def changeStyle(self,styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))




if __name__ == '__main__':



    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
