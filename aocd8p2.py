from math import lcm
data = open('inp8.txt', 'r').readlines()
dirns = {}
curr = []
for i in data[2:]:
    dirns[i[:3]] = (i[7:10], i[12:15])
    if i[2] == 'A':
        curr.append(i[:3])
steps = 0
flag = True
ins = data[0]
flag = True
ans = [-1] * len(curr)
count = 0
while flag:
    for i in data[0][:-1]:
        steps += 1
        if i == 'L':
            for j in range(len(curr)):
                curr[j] = dirns[curr[j]][0]
                if curr[j][-1] == 'Z' and ans[j] == -1:
                    ans[j] = steps
                    count += 1
        else:
            for j in range(len(curr)):
                curr[j] = dirns[curr[j]][1]
                if curr[j][-1] == 'Z' and ans[j] == -1:
                    ans[j] = steps
                    count += 1
    if count == len(curr):
        flag = False
lcm_ans = 1
for i in ans:
    lcm_ans = lcm(lcm_ans, i)
lcm_ans = lcm(len(data[0]) - 1, lcm_ans)
print(lcm_ans)