import re
f = open('inp2.txt', 'r')
lines = f.readlines()
sm = 0
for line in lines:
    red_matches = re.findall(r'(\d+) red', line)
    green_matches = re.findall(r'(\d+) green', line)
    blue_matches = re.findall(r'(\d+) blue', line)
    red_matches = map(int, red_matches)
    green_matches = map(int, green_matches)
    blue_matches = map(int, blue_matches)
    sm += max(red_matches) * max(blue_matches) * max(green_matches)
print(sm)