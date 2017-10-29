import sys
import random
import std_path
import readin
import fgn_2_main
import hill_climbing_main
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

    def compute_initial_figure(self):
        self.axes.plot(readin.readin()[1])

<<<<<<< HEAD
    def update_figure(self,opt_tour = std_path.read_std_path(),dif = 1):
        # 构建4个随机整数，位于闭区间[0, 10]
        #l = [random.randint(0, 10) for i in range(4)]
        lf_title = "Deviation degree:" + str(dif)
        self.axes.title(lf_title)
        self.axes.plot(opt_tour)
=======
    def update_figure(self):
        # 构建4个随机整数，位于闭区间[0, 10]
        l = [random.randint(0, 10) for i in range(4)]

        self.axes.plot([0, 1, 2, 3], l, 'r')
        #SD = hill_climbing_main.dis_cal(std_path)/best_ans*100
        #dif = SD
        #tt = "divention degree:" + str(dif)
        #self.axes.title(tt)
>>>>>>> parent of f711ae6... display updated
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
        self.btn1 = QPushButton("SA", self)
        self.btn1.resize(self.btn1.sizeHint())
        #这里改成连接到fgn_2_main.py的连接
<<<<<<< HEAD
        self.btn1.clicked.connect(SA)
        self.btn1.move(100, 360)
=======
        self.btn1.clicked.connect(QCoreApplication.quit)
        l.addWidget(self.btn1)
>>>>>>> parent of f711ae6... display updated

        #爬山法按钮
        self.btn2 = QPushButton("HC", self)
        self.btn2.resize(self.btn2.sizeHint())
        #这里改成连接到hill_climbing_main.py的连接
        self.btn2.clicked.connect(QCoreApplication.quit)
<<<<<<< HEAD
        self.btn2.move(350, 360)

        #启动按钮
        self.btn3 = QPushButton("LET'S ROCK ON!!!", self)
        self.btn3.resize(self.btn3.sizeHint())
        #这里改成启动程序
        self.btn3.clicked.connect(QCoreApplication.quit)
        self.btn3.move(210, 360)

=======
        l.addWidget(self.btn2)

        #启动按钮
        self.btn3 = QPushButton("LET'S ROCK ON!!!", self)
        self.btn3.resize(self.btn3.sizeHint())
        #这里改成启动程序
        self.btn3.clicked.connect(QCoreApplication.quit)
        l.addWidget(self.btn3)

>>>>>>> parent of f711ae6... display updated
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        # 状态条显示2秒
        #self.statusBar().showMessage("matplotlib 万岁!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About", "no about")

<<<<<<< HEAD
def SA():
	global n,map
	n, map = readin.readin(r"data\eil101.tsp")
	std_path = read_ans.read_ans(n, r"data\eil101.opt.tour")
	ans,path = fgn_2_main.initial()
	
	global t, dis, outer_loop, inner_loop, y
	print(t)
	now_ans, now_path = ans,path					# 初始化设置
	best_ans, best_path = now_ans, now_path
	#print(dis)

	stable = 1
	k = 1
	average = now_ans
	sd = 0

	previous_time = time.time()
#	while  stable < outer_loop:					# 外层循环控制1，通过最优解10000步内不变
	for oloop in range(0,outer_loop):
		if time.time()-previous_time >= 0.5:
			print(t, e)
			std_ans = fgn_2_main.dis_cal(std_path)
			dif = (now_ans-std_ans)/std_ans
			MyDynamicMplCanvas.update_figure([(map[i][0],map[i][1]) for i in now_path],dif)

			previous_time = time.time()
		iloop = inner_loop
		while iloop > 1:			# 内层循环控制，通过迭代的次数

			new_ans, new_path= randomNeighbour(now_ans, now_path)
											# 邻域函数，随机选取一个邻域
			if new_ans < best_ans:
				best_ans = new_ans
				best_path = new_path.copy()
		#		show(best_path)
				stable =0
			else: stable +=1
			if new_ans < now_ans:
				now_ans = new_ans
				now_path = new_path.copy()
			else:
			#	if stable > inner_loop/2:
				e = math.exp((now_ans-new_ans)/(y * t))
			#	else:
			#		e = 0.00001
				if random.random() < e:		# 随机接受
					now_ans = new_ans
					now_path = new_path.copy()
	#		print(stable)
			iloop -=1
	#	t /= math.log(1+k)					# 冷却控制
	#	t /= (1+k)
	#	t -=1
		t *=0.90
	#	average = (average*k + best_ans)/(k+1)
	#	sd = abs((best_ans - average)/average)
	#	if(k>2):iloop = inner_loop/sd
	#	iloop = inner_loop
		k += 1
		if(t < 0.1): break
=======
>>>>>>> parent of f711ae6... display updated

if __name__ == '__main__':
    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("show path")
    aw.show()
    #sys.exit(qApp.exec_())
    app.exec_()
