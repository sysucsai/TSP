import readin
import show_path
import random

n = -1
map = ()


def dis(i,j):
	return ((map[i][0]-map[j][0])**2 + (map[i][1]-map[j][1])**2) ** 0.5


def dis_cal(path):
	back = 0
	for i in range(n):
		back += dis(path[i], path[(i+1)%n])
	return back


def swap(old_ans, old_path, i, j):
	new_path = old_path[0:i] + old_path[j:j+1] + old_path[i+1:j] + old_path[i:i+1] + old_path[j+1:n]
	new_ans = old_ans - dis(old_path[i-1], old_path[i]) - dis(old_path[i], old_path[(i+1)%n]) - \
						dis(old_path[j-1], old_path[j]) - dis(old_path[j], old_path[(j+1)%n]) + \
						dis(new_path[i-1], new_path[i]) + dis(new_path[i], new_path[(i+1)%n]) + \
						dis(new_path[j-1], new_path[j]) + dis(new_path[j], new_path[(j+1)%n])
	return new_ans, new_path


def sa():
	global n, map
	n, map = readin.readin()
	time = 1
	p = 0.8
	delta = ((2/(p*n**2))*((time*(10**7))**(1/n)))**(2/n)
	print("p = ", p, "    delta = ", delta)
	#p = 1; delta = 0.99
	map = tuple(map)
	ans_path = [ i for i in range(n) ]
	#ans_path = [1,14,13,12,7,6,15,5,11,9,10,16,3,2,4,8]
	#ans_path = [i-1 for i in ans_path]
	ans_path = tuple(ans_path)
	ans = dis_cal(ans_path)
	ready = [(ans, ans_path)]
	flag = {ans}
	while len(ready):
		#print(ready[0])
		now_ans, now_path = ready[0]
		del ready[0]
		for i in range(n):
			for j in range(i+1, n):
				if i != j:
					new_ans, new_path= swap(now_ans, now_path, i, j)
					if new_ans < ans:
						ans = new_ans
						ans_path = new_path[:]
						ready.append((new_ans, new_path))
						flag.add(new_path)
						continue
					if new_ans in flag:
						continue
					if random.random() < p:
						ready.append((new_ans,new_path))
						flag.add((new_ans, new_path))
		p *= delta
	return ans, ans_path

if __name__ == "__main__":
	ans, ans_path = sa()
	tmp = [(map[i][0],map[i][1]) for i in ans_path]
	tmp.append((map[ans_path[0]][0], map[ans_path[0]][1]))
	ans_path = list(ans_path)
	for i in range(len(ans_path)):
		ans_path[i] += 1
	print("The ans is ", ans, " : ", ans_path)
	show_path.plot(tmp)
