import readin
import show_path
import random
import math
import read_ans

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


def sa(input):
	global n, map
	n, map = readin.readin(input)
	inital_dis(n, map)
	#print(dis)
	t = 3000
	delta = 0.999
	map = tuple(map)
	now_path = [ i for i in range(n) ]
	now_path = tuple(now_path)
	now_ans = dis_cal(now_path)
	best_ans = now_ans
	best_path = now_path
	count = 0
	random_count = 0
	small_e_count = 0
	while small_e_count < int(n*n/2):
		for iloop in range(int(n*n/2)):
			count += 1
			i = random.randint(0, n - 1)
			j = random.randint(0, n - 1)
			while i >= j:
				i = random.randint(0, n - 1)
				j = random.randint(0, n - 1)
			new_ans, new_path= swap(now_ans, now_path, i, j)
			if new_ans < best_ans:
				best_ans = new_ans
				best_path = new_path
			if new_ans < now_ans:
				now_ans = new_ans
				now_path = new_path
				random_count = 0
			else:
				e = math.exp((now_ans-new_ans)/t)
				if random.random() < e:
					now_ans = new_ans
					now_path = new_path
				elif e < 1e-3:
					small_e_count += 1
				else:
					small_e_count = 0
				random_count += 1
			if random_count > int(n*n/4):
				break
		t *= delta
		print(t, e)
	while 1:
		count += 1
		print(count)
		better_ans = best_ans
		better_path = best_path
		for i in range(n):
			for j in range(n):
				new_ans, new_path = swap(best_ans, best_path, i, j)
				if new_ans < better_ans:
					better_ans = new_ans
					better_path = new_path
		if better_ans > best_ans:
			best_ans = better_ans
			best_path = better_path
		else:
			break
	print("count = ", count)
	return best_ans, best_path

if __name__ == "__main__":
	ans, ans_path = sa(r"data\eil101.tsp")
	print("My ans is ", ans, " : ", ans_path)
	std_path = read_ans.read_ans(n, r"data\eil101.opt.tour")
	print("Standard ans is ", dis_cal(std_path), " : ", std_path)
	tmp = [(map[i][0],map[i][1]) for i in ans_path]
	tmp.append((map[ans_path[0]][0], map[ans_path[0]][1]))
	show_path.plot(tmp)


