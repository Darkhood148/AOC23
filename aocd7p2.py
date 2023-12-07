order = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
def custom_sort(item):
    key_list = [order[char] for char in item[0]]
    return key_list

data = [tuple(i.split()) for i in open('inp7.txt', 'r').readlines()]
fiveoak = []
fouroak = []
fh = []
toak = []
tp = []
op = []
hc = []
for i in data:
    tmp = {}
    for j in i[0]:
        if j in tmp:
            tmp[j] += 1
        else:
            tmp[j] = 1
    if len(tmp) == 5:
        if 'J' in tmp:
            op.append(i)
        else:
            hc.append(i)
    elif len(tmp) == 1:
        fiveoak.append(i)
    elif len(tmp) == 2:
        if tmp[next(iter(tmp))] == 1 or tmp[next(iter(tmp))] == 4:
            if 'J' in tmp:
                fiveoak.append(i)
            else:
                fouroak.append(i)
        else:
            if 'J' in tmp:
                fiveoak.append(i)
            else:
                fh.append(i)
    elif len(tmp) == 4:
        if 'J' in tmp:
            if tmp['J'] == 2:
                toak.append(i)
            else:
                toak.append(i)
        else:
            op.append(i)
    else:
        temp = list(tmp.keys())
        if tmp[temp[0]] == 3 or tmp[temp[1]] == 3 or tmp[temp[2]] == 3:
            if 'J' in tmp:
                fouroak.append(i)
            else:
                toak.append(i)
        else:
            if 'J' in tmp:
                if tmp['J'] == 2:
                    fouroak.append(i)
                else:
                    fh.append(i)
            else:
                tp.append(i)
                
fiveoak = sorted(fiveoak, key=custom_sort)
fouroak = sorted(fouroak, key=custom_sort)
fh = sorted(fh, key=custom_sort)
toak = sorted(toak, key=custom_sort)
tp = sorted(tp, key=custom_sort)
op = sorted(op, key=custom_sort)
hc = sorted(hc, key=custom_sort)

rank = 0
tot = 0

for i in hc:
    rank += 1
    tot += rank * int(i[1])

for i in op:
    rank += 1
    tot += rank * int(i[1])

for i in tp:
    rank += 1
    tot += rank * int(i[1])

for i in toak:
    rank += 1
    tot += rank * int(i[1])

for i in fh:
    rank += 1
    tot += rank * int(i[1])

for i in fouroak:
    rank += 1
    tot += rank * int(i[1])

for i in fiveoak:
    rank += 1
    tot += rank * int(i[1])

print(tot)