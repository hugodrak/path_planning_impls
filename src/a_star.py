import numpy as np
import math
from typing import List, Tuple

class AStar:
	def __init__(self, start, goal, grid):
		self.start = start
		self.goal = goal
		self.grid = grid
		self.open_list = []
		self.closed_list = set()
		self.came_from = {}
		self.g_score = {start: 0}
		self.f_score = {start: self.heuristic(start, goal)}
		self.open_list.append((self.f_score[start], start))

	def heuristic(self, node, goal):
		# Using Manhattan distance as heuristic
		return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

	def get_neighbors(self, node):
		neighbors = []
		directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		for direction in directions:
			neighbor = (node[0] + direction[0], node[1] + direction[1])
			if 0 <= neighbor[0] < len(self.grid) and 0 <= neighbor[1] < len(self.grid[0]):
				if self.grid[neighbor[0]][neighbor[1]] == 0:
					neighbors.append(neighbor)
		return neighbors

	def reconstruct_path(self, current):
		total_path = [current]
		while current in self.came_from:
			current = self.came_from[current]
			total_path.append(current)
		return total_path[::-1]

	def search(self):
		while self.open_list:
			self.open_list.sort()
			current = self.open_list.pop(0)[1]

			if current == self.goal:
				return self.reconstruct_path(current)

			self.closed_list.add(current)

			for neighbor in self.get_neighbors(current):
				if neighbor in self.closed_list:
					continue

				tentative_g_score = self.g_score[current] + 1

				if neighbor not in [i[1] for i in self.open_list]:
					self.open_list.append((self.f_score.get(neighbor, float('inf')), neighbor))
				elif tentative_g_score >= self.g_score.get(neighbor, float('inf')):
					continue

				self.came_from[neighbor] = current
				self.g_score[neighbor] = tentative_g_score
				self.f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.goal)

		return None