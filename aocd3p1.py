import re
def get_regex_matches_indices(pattern, text):
    matches = re.finditer(pattern, text)
    indices = [(match.start(), match.end()) for match in matches]
    return indices

lines = open('inp3.txt', 'r').read().split('\n')
lineinfo = []
for line in lines:
    lineinfo.append(get_regex_matches_indices(r'\d+', line))
sm = 0

for i, data in enumerate(lineinfo):
    for cords in data:
        if i != 0:
            if re.search(r'[^\d\.]' ,lines[i-1][(cords[0]-1 if cords[0] != 0 else 0):(cords[1]+1 if cords[1] != 140 else 140)]):
                sm += int(lines[i][cords[0]:cords[1]])
                continue
        if i != 139:
            if re.search(r'[^\d\.]' ,lines[i+1][(cords[0]-1 if cords[0] != 0 else 0):(cords[1]+1 if cords[1] != 140 else 140)]):
                sm += int(lines[i][cords[0]:cords[1]])
                continue
        if cords[0] != 0:
            if not (lines[i][cords[0]-1].isdigit() or lines[i][cords[0]-1] == '.'):
                sm += int(lines[i][cords[0]:cords[1]])
                continue
        if cords[1] != 140:
            if not (lines[i][cords[1]].isdigit() or lines[i][cords[1]] == '.'):
                sm += int(lines[i][cords[0]:cords[1]])
                continue
print(sm)