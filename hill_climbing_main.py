import readin
import show_path
import random
import math
import read_ans
import matplotlib.pyplot as plt

n = -1
dis = []


def inital_dis(n, map):
	global dis
	for i in range(n):
		dis.append([])
		for j in range(n):
			dis[i].append(((map[i][0]-map[j][0])**2 + (map[i][1]-map[j][1])**2) ** 0.5)
		dis[i] = tuple(dis[i])
	dis = tuple(dis)


def dis_cal(path):
	back = 0
	for i in range(n):
		back += dis[path[i]][path[(i+1)%n]]
	return back


def swap(old_ans, old_path, i, j):
	new_path = old_path[0:i] + old_path[j:j+1] + old_path[i+1:j] + old_path[i:i+1] + old_path[j+1:n]
	if random.random() > 0.01:
		new_ans = old_ans - dis[old_path[i-1]][old_path[i]] - dis[old_path[i]][old_path[(i+1)%n]] - \
							dis[old_path[j-1]][old_path[j]] - dis[old_path[j]][old_path[(j+1)%n]] + \
							dis[new_path[i-1]][new_path[i]] + dis[new_path[i]][new_path[(i+1)%n]] + \
							dis[new_path[j-1]][new_path[j]] + dis[new_path[j]][new_path[(j+1)%n]]
		return new_ans, new_path
	else :
		return dis_cal(new_path), new_path


def test_argu(p, delta):
	count = 1
	print("p = ", p, "    delta = ", delta)
	for i in range(1,n+1):
		count += count * n*(n-1)/2*p
		p = p * delta
	print("p = ", p, "    count = ", count)


def hill_climbing(input):
	global n, map
	#n, map = readin.readin()   #n is the sum of cities, map[i] returns the location of a city(22.11, 45.23)
	#p = 1; delta = 0.99
	#map = tuple(map)
	ans_path = [ i for i in range(n) ]

	ans_path = tuple(ans_path)
	ans = dis_cal(ans_path)

	n, map = readin.readin(input)
	inital_dis(n, map)
	#print(dis)
	map = tuple(map)
	now_path = [ i for i in range(n) ]
	now_path = tuple(now_path)
	now_ans = dis_cal(now_path)
	best_ans = now_ans
	best_path = now_path
	count = 0
	random_count = 0
	small_e_count = 0
	ready = [(now_ans, now_path)]
	flag = {ans}
	while len(ready):
		now_ans, now_path = ready[0]
		del ready[0]
		count += 1
		print(count)
		for i in range(n):
			for j in range(i+1,n):
				if i != j:
					new_ans, new_path = swap(now_ans, now_path, i, j)
					if new_ans < best_ans:
						best_ans = new_ans
						best_path = new_path[:]
						ready.append((new_ans, new_path))
						flag.add(new_path)
						tmp = [(map[m][0],map[m][1]) for m in best_path]
						tmp.append((map[best_path[0]][0], map[best_path[0]][1]))
						plt.scatter(*zip(*tmp))
						plt.plot(*zip(*tmp))
						plt.pause(0.01)
						plt.clf()
						continue
					if new_ans in flag:
						tmp = [(map[m][0],map[m][1]) for m in best_path]
						tmp.append((map[best_path[0]][0], map[best_path[0]][1]))
						plt.scatter(*zip(*tmp))
						plt.plot(*zip(*tmp))
						plt.pause(0.01)
						plt.clf()
						continue

	print("step taken: ", count)
	return best_ans, best_path

if __name__ == "__main__":
	ans, ans_path = hill_climbing(r"data\att48.tsp")
	print("My ans is ", ans, " : ", ans_path)
	std_path = read_ans.read_ans(n, r"data\att48.opt.tour")
	print("Standard ans is ", dis_cal(std_path), " : ", std_path)
	SD = dis_cal(std_path)/ans*100
	print("Similar degree is ", SD, "%.")
	tmp = [(map[i][0],map[i][1]) for i in ans_path]
	tmp.append((map[ans_path[0]][0], map[ans_path[0]][1]))
	show_path.plot(tmp,0)
