ans = sum([(1 << 36 - len(set(i[10:-1].split())))//2 for i in open('inp4.txt', 'r').readlines()])
print(ans)