import time
st = time.time()
txt = open('inp1.txt', 'r').read()
txt += '\n'
d1 = None
d2 = None
sm = 0
i = 0
txt_len = len(txt)
while i < txt_len:
    if txt[i].isdigit():
        if d1:
            d2 = txt[i]
        else:
            d1 = txt[i]
    elif txt[i] == '\n':
        if d2:
            sm += int(d1+d2)
        else:
            sm += int(d1+d1)
        d1 = None
        d2 = None
    else:
        fiv = fur = thr = None
        if i + 5 <= txt_len:
            fiv = txt[i:i+5]
        if i + 4 <= txt_len:
            fur = txt[i:i+4]
        if i + 3 <= txt_len:
            thr = txt[i:i+3]
        if fiv == 'three':
            if d1:
                d2 = '3'
            else:
                d1 = '3'
            i += 4
            continue
        elif fiv == 'seven':
            if d1:
                d2 = '7'
            else:
                d1 = '7'
            i += 4
            continue
        elif fiv == 'eight':
            if d1:
                d2 = '8'
            else:
                d1 = '8'
            i += 4
            continue
        elif fur == 'four':
            if d1:
                d2 = '4'
            else:
                d1 = '4'
            i += 4
            continue
        elif fur == 'five':
            if d1:
                d2 = '5'
            else:
                d1 = '5'
            i += 3
            continue
        elif fur == 'nine':
            if d1:
                d2 = '9'
            else:
                d1 = '9'
            i += 3
            continue
        elif thr == 'one':
            if d1:
                d2 = '1'
            else:
                d1 = '1'
            i += 2
            continue
        elif thr == 'two':
            if d1:
                d2 = '2'
            else:
                d1 = '2'
            i += 2
            continue
        elif thr == 'six':
            if d1:
                d2 = '6'
            else:
                d1 = '6'
            i += 3
            continue
    i+=1
print(sm)