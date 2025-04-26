from pathlib import Path
import re
import math

path = Path("./data/day3.txt")

data = ''
with open(path, "r") as f:
    for line in f.read():
        data += line

hits = [a.start() for a in list(re.finditer('mul', data))]

sub_list =[]
for hit in hits:
    sub = data[hit+4:hit+13].split(',')
    try:
        piece = [int(sub[0]), int(sub[1].split(')')[0])]
        sub_list.append(piece)
    except:
        print(sub)

result = 0
for sub in sub_list:
    result += math.prod(sub)

print("result 1 = ", result) #179571322