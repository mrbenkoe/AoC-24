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

print("rules =",rules)
print("updates =",updates)

result =[]
for i, update in enumerate(updates):
    a = list(map(list, combinations(update, 2)))
    counter = 0
    for item in a:
        for rule in rules:
            if item == rule:
                counter += 1
    if counter == len(a):  
        result.append(update[int(len(update)/2)])

print("result =", sum(result)) #5087


