from pathlib import Path
import numpy as np
import sys

file = "day6.txt"

path = Path("./data/"+file)

data = []
with open(path, "r") as f:
    for line in f.read().splitlines():
        data.append(line)

def change_direction(m):
    m += 1
    if m > 3:
        m = 0
    dir = moves[m]
    return m, dir

def check_next(pos, dir, m): 
    next = [pos[0] + dir[0], pos[1] + dir[1]]

    if next[0] < len(data) and next[1] < len(data[0]):

        if data[next[0]][next[1]] in [".", "^"]:
            new_pos = next
        elif data[next[0]][next[1]] == "#":
            new_pos = pos
            m, dir = change_direction(m)
        else:
            return "Error"
    else:
        print("result =", len(list(set(tuple(pos) for pos in visited)))) #5404
        sys.exit()

    return new_pos, dir, m

for li, line in enumerate(data):
    if line.find("^") > 0:
        start = [li, line.find("^")]

moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

pos, dir, m = start, moves[0], 0

visited = [pos]

while True:
    pos, dir, m = check_next(pos, dir, m)
    print("check_next =", pos, dir, m)
    visited.append(pos)