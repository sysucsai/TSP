import matplotlib.pyplot as plt

def plot(city_coordinate):
	'''使用这个函数前必须安装包，请使用“pip install matplotlib”包
	传进来一个关于城市坐标的list即可，如：
	[(38.24, 20.42), (39.57, 26.15), (40.56, 25.32), (36.26, 23.12), (33.48, 10.54), (37.56, 12.19)]'''
	plt.clf()
	plt.scatter(*zip(*city_coordinate))
	plt.plot(*zip(*city_coordinate))
	plt.show()

def animation(city_coordinate):
	plt.clf()
	plt.scatter(*zip(*city_coordinate))
	plt.plot(*zip(*city_coordinate))
	plt.pause(0.000001)
