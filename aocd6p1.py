import re, math
f = open('inp6.txt', 'r').readlines()
times = list(map(int, re.findall(r'\d+', f[0])))
dis = list(map(int, re.findall(r'\d+', f[1])))
prod = 1
for i in range(len(times)):
    val1 = math.floor((times[i] - math.sqrt(times[i] * times[i] - 4 * dis[i]))/2) + 1
    val2 = math.ceil((times[i] + math.sqrt(times[i] * times[i] - 4 * dis[i]))/2) - 1
    prod *=(val2 - val1 + 1)
print(prod)