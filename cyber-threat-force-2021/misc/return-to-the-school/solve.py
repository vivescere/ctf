import math
from pwn import *
from astar import AStar

def parse_maze(source):
        source = source.strip()
        source = source.split('\n')
        source = source[:-1]  # Remove last line (dots)
        source = [list(l[1:-1]) for l in source]  # Remove left and right dots
        return source

# Mostly copied from the astar package example.
class MazeSolver(AStar):

        def __init__(self, maze):
                self.maze = maze
                self.height = len(maze)
                self.width = len(maze[0])

        def heuristic_cost_estimate(self, n1, n2):
                (x1, y1) = n1
                (x2, y2) = n2
                return math.hypot(x2 - x1, y2 - y1)

        def distance_between(self, n1, n2):
                return 1

        def neighbors(self, node):
                x, y = node
                return [
                        (nx, ny)
                        for nx, ny
                        in [
                                (x, y - 1),
                                (x, y + 1),
                                (x - 1, y),
                                (x + 1, y)
                        ]
                        if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == ' '
                ]

def sol_to_dir(i):
        last = None
        steps = []

        for element in i:
                if last is None:
                        last = element
                        continue

                old_x, old_y = last
                x, y = element

                if old_x < x:
                        steps.append('O')
                elif old_x > x:
                        steps.append('E')
                elif old_y < y:
                        steps.append('S')
                elif old_y > y:
                        steps.append('N')
                else:
                        raise RuntimeError('should not happen')

                last = element

        return steps

r = remote('XXX.XXX.XXX.XXX', 00000)

header = r.recvuntil(b'.' * 92).decode()
maze = parse_maze(r.recvuntil(b'.' * 92).decode())

width = len(maze[0])
height = len(maze)

# We want the path from the bottom right corner, to the top left one.
start = (width - 1, height - 1)
goal = (0, 0)

solution = list(MazeSolver(maze).astar(start, goal))
solution = ''.join(sol_to_dir(solution))

r.send(f'{solution}\n')

print('---------------')
print(r.recvall().decode())

r.close()

