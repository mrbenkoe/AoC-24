from pathlib import Path
import numpy as np
from itertools import combinations

file = "day5.txt"
path = Path("./data/"+file)

rules = []
updates = []
with open(path, "r") as f:
    for line in f.read().splitlines():
        if '|' in line:
            rules.append(list(map(int, line.split('|'))))
        elif ',' in line:
            updates.append(list(map(int, line.split(','))))

result = []
incorrect = []
for i, update in enumerate(updates):
    a = list(map(list, combinations(update, 2)))
 
    counter = 0
    for item in a:
        for rule in rules:
            if item == rule:
                counter += 1
    if counter == len(a):  
        result.append(update[int(len(update)/2)])
    else:
        incorrect.append(update)

print("result =", sum(result)) #5087

result = 0
for i, update in enumerate(incorrect):
    for j in range(5):
        for r in rules:
            if len([x for x in update if x in r]) == 2:
                index_0 = update.index(r[0])
                index_1 = update.index(r[1])
                if index_0 > index_1:
                    update[index_0] = r[1]
                    update[index_1] = r[0]

    result += update[int(len(update)/2)]

print("result =", result) #4971