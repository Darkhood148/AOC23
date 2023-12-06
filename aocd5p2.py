data = open('inp5.txt', 'r').read().split('\n\n')
sp = data[0].split()
seeds = tuple((int(sp[i]), int(sp[i+1])) for i in range(1, len(sp), 2))
spl_data = []
for i in data[1:]:
    tmp = []
    for j in i.split('\n')[1:]:
        tmp.append(tuple(map(int, j.split())))
    tmp = sorted(tmp, key=lambda x: x[1])
    lenn = len(tmp)
    if tmp[0][1] != 0:
        tmp.append((0, 0, tmp[0][1]))
    for j in range(lenn-1):
        if tmp[j][1] + tmp[j][2] != tmp[j+1][1]:
            tmp.append((tmp[j][1] + tmp[j][2], tmp[j][1] + tmp[j][2], tmp[j+1][1] - tmp[j][1] - tmp[j][2]))
    tmp.append((tmp[lenn-1][1] + tmp[lenn-1][2], tmp[lenn-1][1] + tmp[lenn-1][2], 9999999999 - tmp[lenn-1][1] - tmp[lenn-1][2]))
    spl_data.append(tmp)

copies = tuple(seeds)
copies2 = []
for i in spl_data:
    for j in i:
        for k in copies:
            if not(k[0] >= j[1] + j[2] or k[0] + k[1] <= j[1]):
                minn = max(k[0], j[1])
                maxx = min(k[0] + k[1], j[1] + j[2])
                lenn = maxx - minn
                star = minn - j[1] + j[0]
                copies2.append((star, lenn))
    copies = tuple(copies2)
    copies2 = []

print(min(copies, key=lambda x: x[0])[0])