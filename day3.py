from pathlib import Path
import re
import math

path = Path("./data/day3.txt")

data = ''
with open(path, "r") as f:
    for line in f.read():
        data += line

def check(data):

    hits = [a.start() for a in list(re.finditer('mul', data))]

    sub_list =[]
    for hit in hits:
        sub = data[hit+4:hit+13].split(',')
        try:
            piece = [int(sub[0]), int(sub[1].split(')')[0])]
            sub_list.append(piece)
        except:
            pass

    return sub_list

sub_list = check(data)

result = 0
for sub in sub_list:
    result += math.prod(sub)

print("result 1 = ", result) #179571322

dont = list([a.start() for a in re.finditer("don't()", data)])

do = [0] + list(set([a.start() for a in re.finditer("do()", data)]) - set(dont))

pkg = [[0, "do"]]
for i in range(len(data)):
    if i in do and pkg[-1][1] != "do":
        pkg.append([i, "do"])
    elif i in dont and pkg[-1][1] != "dont":
        pkg.append([i, "dont"])

ranges = list([item[0] for item in pkg])+[len(data)]

n = 2
split_ranges = [ranges[i:i + n] for i in range(0, len(ranges), n)]

sub_list = []
for sr in split_ranges:
    x = check(data[sr[0]:sr[1]])
    sub_list.append(x)

sub_list = sum(sub_list, [])

result = 0
for sub in sub_list:
    result += math.prod(sub)

print("result 2 = ", result) #103811193