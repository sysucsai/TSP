import re
import read_ans
import readin


def read_std_path(file = r"data\eil101.opt.tour"):
	global n,map
	n, map = readin.readin(r"data\eil101.tsp")
	std_path = read_ans.read_ans(n, file)
	return [(map[i][0],map[i][1]) for i in std_path]

if __name__ == '__main__':
	'''运行sample'''
	#show_path.plot(read_std_path()[1])