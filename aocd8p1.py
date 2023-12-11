data = open('inp8.txt', 'r').readlines()
dirns = {}
for i in data[2:]:
    dirns[i[:3]] = (i[7:10], i[12:15])
steps = 0
flag = True
ins = data[0]
flag = True
curr = 'AAA'
while flag:
    for i in data[0][:-1]:
        if i == 'L':
            curr = dirns[curr][0]
        else:
            curr = dirns[curr][1]
    steps += len(data[0]) - 1
    if curr == 'ZZZ':
        flag = False
print(steps)