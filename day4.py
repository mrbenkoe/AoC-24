from pathlib import Path
import numpy as np

file = "day4.txt"
path = Path("./data/"+file)

data = []
with open(path, "r") as f:
    for line in f.read().splitlines():
        data.append(list(line))

data = np.array(data, dtype=str)

df = np.zeros((len(data)+6, len(data[0])+6), dtype=str)

df[3:-3, 3:-3] = data

rows, cols = [[-1,-2,-3],[0,0,0],[1,2,3]], [[-1,-2,-3],[0,0,0],[1,2,3]]

result = 0 
for i in range(3,len(df[0])-3):
    for j in range(3,len(df[1])-3):
        if df[i,j] == "X":
            for row in rows:
                for col in cols:
                    if df[i+row[0],j+col[0]] == "M" and df[i+row[1],j+col[1]] == 'A' and df[i+row[2],j+col[2]] == 'S':
                        result += 1

print(result)
