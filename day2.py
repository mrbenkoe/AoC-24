from pathlib import Path

file = "day2.txt"
path = Path("./data/"+file)

data = []
with open(path, "r") as f:
    for line in f.read().splitlines():
        data.append(list(map(int, line.split())))

def check(data):
    res = 0
    check = 0
    if all(val > 0 for val in data) or all(val < 0 for val in data):
        check += 1
    if all(abs(val) < 4 for val in data):
        check += 1
    if check == 2:
        res = 1
    return res

result = 0
for report in data:
    analysis = []
    for li, level in enumerate(report[:-1]):
        analysis.append(report[li+1]-report[li])

    result += check(analysis)

print("result 1 = ", result)

result = 0
for report in data:

    x = 0
    for i in range(len(report)):
        small = report[:i]+report[i+1:]

        analysis = []
        for li, level in enumerate(small[:-1]):
            analysis.append(small[li+1]-small[li])

        x += check(analysis)
    if x > 0:
        result += 1

print("result 2 = ", result)