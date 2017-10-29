import sys
import random
import std_path
import readin
import fgn_2_main
import hill_climbing_main
import sa
#这里要import原主函数里的“头文件”
import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

mode = 0

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)
        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class MyStaticMplCanvas(MyMplCanvas):
    def compute_initial_figure(self):
        opt_tour = std_path.read_std_path()
        self.axes.scatter(*zip(*opt_tour))
        self.axes.plot(*zip(*opt_tour))

class MyDynamicMplCanvas(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)
        if mode == 0:
            self.obj = sa.Sa(r"data\eil101.tsp")
        else:
            self.obj = hc.Hc(r"data\eil101.tsp")

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        objec = Sa(r"data\eil101.tsp")
        # 构建4个随机整数，位于闭区间[0, 10]
        #if mode == 0:


        #else:


        l = self.obj.next()
        #l = [random.randint(0, 10) for i in range(4)]

        self.axes.plot([0, 1, 2, 3], l, 'r')
        #SD = hill_climbing_main.dis_cal(std_path)/best_ans*100
        #dif = SD
        #tt = "divention degree:" + str(dif)
        #self.axes.title(tt)
        self.draw()

class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("程序主窗口")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QWidget(self)

        l = QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)
        l.addWidget(dc)



        #模拟退火法按钮
        self.btn1 = QPushButton("Simulate Anneal", self)
        self.btn1.resize(self.btn1.sizeHint())
        #这里改成连接到fgn_2_main.py的连接
        self.btn1.clicked.connect(decide_SA)
        l.addWidget(self.btn1)

        #爬山法按钮
        self.btn2 = QPushButton("Hill Climbing", self)
        self.btn2.resize(self.btn2.sizeHint())
        #这里改成连接到hill_climbing_main.py的连接
        self.btn2.clicked.connect(decide_HC)
        l.addWidget(self.btn2)


        # 状态条显示2秒
        #self.statusBar().showMessage("matplotlib 万岁!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About", "no about")

    def decide_SA():
        mode = 0

    def decide_HC():
        mode = 1


if __name__ == '__main__':
    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("show path")
    aw.show()
    #sys.exit(qApp.exec_())
    app.exec_()
