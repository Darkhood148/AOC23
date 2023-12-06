import re, math
f = open('inp6.txt', 'r').readlines()
t = ''
d = ''
for i in re.findall(r'\d+', f[0]):
    t += i
t = int(t)

for i in re.findall(r'\d+', f[1]):
    d += i
d = int(d)

val1 = math.floor((t - math.sqrt(t * t - 4 * d))/2) + 1
val2 = math.ceil((t + math.sqrt(t * t - 4 * d))/2) - 1
print(val2 - val1 + 1)