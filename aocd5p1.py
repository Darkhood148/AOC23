data = open('inp5.txt', 'r').readlines()
seeds = tuple(int(i) for i in data[0].split()[1:])
copies = tuple(seeds)
num_seeds = len(seeds)
copies2 = list(copies)
for line in data[1:]:
    temp = line.split()
    if len(temp) == 3:
        for i in range(num_seeds):
            if copies[i] >= int(temp[1]) and copies[i] < int(temp[1]) + int(temp[2]):
                copies2[i] = int(temp[0]) + copies[i] - int(temp[1])
    if len(temp) == 0:
        copies = tuple(copies2)
print(min(copies2))