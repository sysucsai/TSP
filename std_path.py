import re
import read_ans
import readin


def read_std_path(file = r"data\eil101.opt.tour"):
	global n,map
	n, map = readin.readin(r"data\eil101.tsp")
	std_path = read_ans.read_ans(n, file)
	opt_tour = [(map[i][0],map[i][1]) for i in std_path]
	opt_tour.append((map[std_path[0]][0], map[std_path[0]][1]))
	return opt_tour

if __name__ == '__main__':
	'''运行sample'''
	#show_path.plot(read_std_path()[1])
