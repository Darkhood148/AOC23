tot = 0
txt = open('inp2.txt', 'r').read()
txt+='\nGame'
words = txt.split()
curr = 0
flag = True
su = 0
for i, word in enumerate(words):
    if word[:4] == 'Game':
        if flag:
            su += curr
        flag = True
        curr += 1
    elif word == 'blue' or word == 'blue;' or word == 'blue,':
        if not int(words[i-1]) <= 14:
            flag = False
    elif word == 'green' or word == 'green;' or word == 'green,':
        if not int(words[i-1]) <= 13:
            flag = False
    elif word == 'red' or word == 'red;' or word == 'red,':
        if not int(words[i-1]) <= 12:
            flag = False
print(su)