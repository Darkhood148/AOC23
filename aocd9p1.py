data = [i.split() for i in [j for j in open('inp9.txt', 'r').readlines()]]
for i in range(len(data)):
    data[i] = list(map(int, data[i]))
su = 0
for i in data:
    curr = [i[0]]
    for j in i[1:]:
        temp = []
        temp.append(j)
        for k in range(len(curr)):
            temp.append(temp[k]-curr[k])
        curr = temp
    su += sum(curr)
print(su)