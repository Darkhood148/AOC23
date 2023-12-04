f = open('inp1.txt', 'r')
d1=0
d2=0
sm = 0
for line in f:
    for i in line:
        if i.isdigit():
            d1=i
            break
    for i in line[::-1]:
        if i.isdigit():
            d2=i
            break
    sm += int(d1+d2)
print(sm)