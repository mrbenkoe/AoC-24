from pathlib import Path
import os
import numpy as np

file = "day1.txt"

path = Path("./data/"+file)

data = []
with open(path, "r") as f:
    for line in f.read().splitlines():
        data.append(line.split())

data = np.array(data, dtype=int)

#print(data)

col_1 = np.sort(data[:, 0])
col_2 = np.sort(data[:, 1])

result = sum(abs(col_2-col_1))

print("result 1 = ",result)


