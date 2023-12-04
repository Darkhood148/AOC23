data = [36 - len(set(i[10:-1].split())) for i in open('inp4.txt', 'r').readlines()]
to_be_added = [1] + [0] * 201
curr_quantity = 0
total = 0
for i in range(201):
    curr_quantity += to_be_added[i]
    total += curr_quantity
    to_be_added[i+1] += curr_quantity
    to_be_added[i+data[i]+1] -= curr_quantity
print(total)