import readin
import time
import random
import math
import show_path

class Hc:
	def __init__(self, input, frequency = 0.2, t = 3000,  delta = 0.99):
		self.n, self.map = readin.readin(input)
		self.initial_dis(self.n, self.map)
		self.map = tuple(self.map)
		self.now_path = [i for i in range(self.n)]
		self.now_ans = self.dis_cal(self.now_path)
		self.best_ans = self.now_ans
		self.best_path = self.now_path[:]
		self.count = 0
		self.small_e_count = 0
		self.t = t
		self.delta = delta
		self.finish = False
		self.frequency = frequency

	def initial_dis(self, n, map):
		self.dis = []
		for i in range(n):
			self.dis.append([])
			for j in range(n):
				self.dis[i].append(((map[i][0]-map[j][0])**2 + (map[i][1]-map[j][1])**2) ** 0.5)
			self.dis[i] = tuple(self.dis[i])
		self.dis = tuple(self.dis)

	def dis_cal(self, path):
		back = 0
		for i in range(self.n):
			back += self.dis[path[i]][path[(i + 1) % self.n]]
		return back

	def dis_cal(self, path):
		back = 0
		for i in range(self.n):
			back += self.dis[path[i]][path[(i + 1) % self.n]]
		return back

	def swap(self, path, i, j):
		tmp = path[i]
		path[i] = path[j]
		path[j] = tmp

	def swap_cal(self, ans, path, i, j):
		if random.random() > 0.01:
			ans -= self.dis[path[i - 1]][path[i]] + self.dis[path[i]][path[(i + 1) % self.n]] + \
				   self.dis[path[j - 1]][path[j]] + self.dis[path[j]][path[(j + 1) % self.n]]
			self.swap(path, i, j)
			ans += self.dis[path[i - 1]][path[i]] + self.dis[path[i]][path[(i + 1) % self.n]] + \
				   self.dis[path[j - 1]][path[j]] + self.dis[path[j]][path[(j + 1) % self.n]]
			return ans, path
		else:
			self.swap(path, i, j)
			return self.dis_cal(path), path

	def next(self):
		better_ans = self.best_ans
		better_path = self.best_path[:]
		for i in range(self.n):
			for j in range(self.n):
				new_ans, new_path = self.swap_cal(self.best_ans, self.best_path, i, j)
				if new_ans < better_ans:
					better_ans = new_ans
					better_path = new_path[:]
				self.swap(self.best_path, i, j)
		if better_ans < self.best_ans:
			self.best_ans = better_ans
			self.best_path = better_path[:]
			return [(self.map[i][0], self.map[i][1]) for i in self.best_path]
		else:
			self.finish = True
			return [(self.map[i][0], self.map[i][1]) for i in self.best_path]

	def get_dif(self):
		self.dif = (self.now_ans - self.best_ans) / self.best_ans


if __name__ == "__main__":
	obj = Hc(r"data\eil101.tsp")
	while obj.finish == False:
		show_path.animation_only_myAns(obj.next())