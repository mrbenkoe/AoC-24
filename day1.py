from pathlib import Path
import numpy as np

file = "day1.txt"

path = Path("./data/"+file)

data = []
with open(path, "r") as f:
    for line in f.read().splitlines():
        data.append(line.split())

data = np.array(data, dtype=int)

#print(data)

col1 = np.sort(data[:, 0])
col2 = np.sort(data[:, 1])

result = sum(abs(col2-col1))

print("result 1 = ", result)

result2 = 0
for val in list(col1):
    result2 += val*list(col2).count(val)

print("result 2 = ", result2)