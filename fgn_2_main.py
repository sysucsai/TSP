import readin
import show_path
import random
import math
import read_ans
import time

const_t = 10

'''def show(path):
	temp = []
	for j in range(n):
		temp.append((map[path[j]][0], map[path[j]][1]))
	show_path.animation(temp, std_path, dif)'''


def randomNeighbour(now_ans, now_path):
	new_path = now_path.copy()
	i = random.randint(0,n-1)
	j = random.randint(0,n-1)
	temp = new_path[i]
	new_path[i] = new_path[j]
	new_path[j] = temp
	new_ans = dis_cal(new_path)
	return new_ans, new_path

def initial_dis():
	global dis
	dis = []
	for i in range(n):
		dis.append([])
		for j in range(n):
			dis[i].append(((map[i][0]-map[j][0])**2 + (map[i][1]-map[j][1])**2) ** 0.5)

def randomSolution(ans, path):
	tmp_ans = ans
	tmp_path = path.copy()
	for i in range(0,2*n):
		tmp_ans, tmp_path = randomNeighbour(tmp_ans, tmp_path)
	return tmp_ans, tmp_path

def initial_t(ans, path, i):
	global t, n, const_t
	best_ans = ans
	best_path = path.copy()
	if(i==0):
		t = const_t
	if(i==1):		# 抽样方差
		average = 0
		tmp = []
		sd = 0
		k = 0
		for j in range(0,n):
			tmp_ans,tmp_path = randomSolution(ans,path)
			average += tmp_ans
			tmp.append(tmp_ans)
			if(tmp_ans<best_ans):
				best_ans = tmp_ans
				best_path = tmp_path.copy()
			k +=1
		average = average/k
		for j in range(0,k):
			sd = (tmp[j] - average)**2
		sd = sd/k
		t = average
	return best_ans,best_path


def dis_cal(path):

	back = 0
	for i in range(n):
		back += dis[path[i]][path[(i+1)%n]]
	return back

def dis_update(old_ans,i,j):
	return 5000

def initial():
	global n, outer_loop, inner_loop, y
	initial_dis()								# 初始化距离表
	now_path = [ i for i in range(n) ]			# 初始化路径
	now_ans = dis_cal(now_path)					# 初始化当前解
	now_ans, now_path = randomSolution(now_ans, now_path)
	now_ans, now_path = initial_t(now_ans, now_path, 1)				# 初温
	outer_loop = 400
	inner_loop = n**2
	y = 1
	return now_ans, now_path


def initial2(ans,path):
	global n,t, outer_loop, inner_loop, y
	initial_t(ans, path, 1)				# 初温
	outer_loop = 400
	inner_loop = n**2
	y = 1


def sa(ans,path,std_path):
	global n, t, map, dis, outer_loop, inner_loop, y
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

			dif = e
			show_path.animation([(map[i][0],map[i][1]) for i in now_path], std_path, dif)

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
		if(t < 0.1): break					# 外层循环控制2，通过温度阈值

	return best_ans, best_path

def test():
	global t, outer_loop, inner_loop, y
	min = 100000000
	mint = 0
	minouterloop = 0
	mininnerloop = 0
	miny = 0
	for i in range(7,15,1):
		for j in range(1000,5000,1000):
			for k in range(10000,20000,1000):
				for x in range(1,8,1):
					t = i
					outer_loop = j
					inner_loop = k
					y = x
					ans, ans_path = sa(r"data\ch130.tsp")
					t = i
					outer_loop = j
					inner_loop = k
					y = x
					print("temp: ",t," outerloop: ",outer_loop," innerloop : ",inner_loop," coeficient: ",y," ans : ",ans)
					if(ans<min):
						min = ans
						mint = i
						minouterloop = j
						mininnerloop = k
						miny = x
	print("best status is ",mint,minouterloop,mininnerloop,miny,"for ans : ",min)


if __name__ == "__main__":
	global n,map
	n, map = readin.readin(r"data\eil101.tsp")
	std_path = read_ans.read_ans(n, r"data\eil101.opt.tour")
	#show_path.initialize(std_path)
	now_ans,now_path = initial()
	ans, ans_path = sa(now_ans,now_path,std_path)
	print("My ans is ", ans, " : ", ans_path)
	'''std_ans = dis_cal(std_path)
	dif = (ans-std_ans)/std_ans
	print("Standard ans is ", std_ans, " : ", std_path)
	print("different = ",(ans-std_ans)/std_ans*100)'''
#	show(std_path)
