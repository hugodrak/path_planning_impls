import numpy as np
import math
from typing import List, Tuple

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.cost = 0

def distance(a: Node, b: Node) -> float:
    return math.hypot(a.x - b.x, a.y - b.y)

def rrt_star(start, goal, obstacle_list, max_iter=500, step_size=5.0, radius=10.0):
    """
    RRT* algorithm implementation.
    """
    # Initialize tree
    nodes = [Node(start[0], start[1])]
    for i in range(max_iter):
        # Sample random point
        rand_x, rand_y = np.random.uniform(0, 100), np.random.uniform(0, 100)
        # Find nearest node
        nearest_node = min(nodes, key=lambda n: distance(n, Node(rand_x, rand_y)))
        # Expand towards random point
        # ...

    # Return final path
    # ...
    return []

if __name__ == "__main__":
    path = rrt_star((0,0), (50,50), obstacle_list=[])
    print("Found path:", path)