import readin
import show_path
import random
import math
import read_ans
import time
import matplotlib.pyplot as plt

n = -1
dis = []


def initial_dis(n, map):
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


def swap(path, i, j):
	tmp = path[i]
	path[i] = path[j]
	path[j] = tmp


def swap_cal(ans, path, i, j):
	if random.random() > 0.01:
		ans -= dis[path[i-1]][path[i]] + dis[path[i]][path[(i+1)%n]] + \
			   dis[path[j-1]][path[j]] + dis[path[j]][path[(j+1)%n]]
		swap(path, i, j)
		ans += dis[path[i - 1]][path[i]] + dis[path[i]][path[(i + 1) % n]] + \
			   dis[path[j - 1]][path[j]] + dis[path[j]][path[(j + 1) % n]]
		return ans, path
	else :
		swap(path, i, j)
		return dis_cal(path), path


def test_argu(p, delta):
	count = 1
	print("p = ", p, "    delta = ", delta)
	for i in range(1,n+1):
		count += count * n*(n-1)/2*p
		p = p * delta
	print("p = ", p, "    count = ", count)


def sa(input, t = 3000,  delta = 0.99):
	global n, map
	n, map = readin.readin(input)
	initial_dis(n, map)
	map = tuple(map)
	now_path = [ i for i in range(n) ]
	now_ans = dis_cal(now_path)
	best_ans = now_ans
	best_path = now_path[:]
	count = 0
	#random_count = 0
	small_e_count = 0
	previous_time = time.time()
	while small_e_count < int(n*n):
		if time.time()-previous_time >= 0.5:
			print(t, e)
			show_path.animation([(map[i][0],map[i][1]) for i in now_path])
			previous_time = time.time()
		for iloop in range(int(n*n)):
			count += 1
			i = random.randint(0, n - 1)
			j = random.randint(0, n - 1)
			while i >= j:
				i = random.randint(0, n - 1)
				j = random.randint(0, n - 1)
			new_ans, now_path= swap_cal(now_ans, now_path, i, j)
			if new_ans < best_ans:
				best_ans = new_ans
				best_path = now_path[:]
			if new_ans < now_ans:
				now_ans = new_ans
			else:
				if t < 100:
					e = math.exp((now_ans-new_ans)/t)
				else :
					e = math.exp((best_ans - new_ans) / t)
				if random.random() < e:
					now_ans = new_ans
				else :
					swap(now_path, i, j)
					if e < 1e-3:
						small_e_count += 1
					else:
						small_e_count = 0
		t *= delta
	while 1:
		count += 1
		print(count)
		better_ans = best_ans
		better_path = best_path[:]
		for i in range(n):
			for j in range(n):
				new_ans, new_path = swap_cal(best_ans, best_path, i, j)
				if new_ans < better_ans:
					better_ans = new_ans
					better_path = new_path[:]
				swap(best_path, i, j)
		if better_ans > best_ans:
			best_ans = better_ans
			best_path = better_path[:]
		else:
			break
	print("count = ", count)
	return best_ans, best_path

if __name__ == "__main__":
	ans, ans_path = sa(r"data\eil101.tsp")
	print("My ans is ", ans, " : ", ans_path)
	std_path = read_ans.read_ans(n, r"data\eil101.opt.tour")
	print("Standard ans is ", dis_cal(std_path), " : ", std_path)
	print("The relative error is ", (ans-dis_cal(std_path))/dis_cal(std_path)*100, "%")
	tmp = [(map[i][0],map[i][1]) for i in ans_path]
	tmp.append((map[ans_path[0]][0], map[ans_path[0]][1]))
show_path.plot(tmp)