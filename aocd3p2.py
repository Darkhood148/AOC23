import re
def get_regex_matches_indices(pattern, text):
    matches = re.finditer(pattern, text)
    indices = [match.start() for match in matches]
    return indices
lines = ['...' + i + '...' for i in open('inp3.txt', 'r').read().split('\n')]
lines = ['.'*146] + lines + ['.'*146]
lineinfo = []
for line in lines:
    lineinfo.append(get_regex_matches_indices(r'[\*]', line))
sm = 0
for i, line in enumerate(lineinfo):
    for cords in line:
        nums = []
        if lines[i-1][cords].isdigit():
            tmp1 = re.findall(r'\d+', lines[i-1][cords-1:cords+2])
            tmp2 = re.findall(r'\d+', lines[i-1][cords-2:cords+1])
            tmp3 = re.findall(r'\d+', lines[i-1][cords:cords+3])
            if len(tmp1) == len(tmp2) == len(tmp3):
                nums.append(str(max(int(tmp1[0]), max(int(tmp2[0]), int(tmp3[0])))))
            elif len(tmp1) == len(tmp2):
                nums.append(str(max(int(tmp1[0]), int(tmp2[0]))))
            elif len(tmp1) == len(tmp3):
                nums.append(str(max(int(tmp1[0]), int(tmp3[0]))))
            else:
                nums.append(tmp1[0])
        else:
            tmp1 = re.findall(r'\d+', lines[i-1][cords-3:cords])
            tmp2 = re.findall(r'\d+', lines[i-1][cords+1:cords+4])
            if len(tmp1) > 0 and lines[i-1][cords-1].isdigit():
                nums.append(tmp1[-1])
            if len(tmp2) > 0 and lines[i-1][cords+1].isdigit():
                nums.append(tmp2[0])
        if lines[i+1][cords].isdigit():
            tmp1 = re.findall(r'\d+', lines[i+1][cords-1:cords+2])
            tmp2 = re.findall(r'\d+', lines[i+1][cords-2:cords+1])
            tmp3 = re.findall(r'\d+', lines[i+1][cords:cords+3])
            if len(tmp1) == len(tmp2) == len(tmp3):
                nums.append(str(max(int(tmp1[0]), max(int(tmp2[0]), int(tmp3[0])))))
            elif len(tmp1) == len(tmp2):
                nums.append(str(max(int(tmp1[0]), int(tmp2[0]))))
            elif len(tmp1) == len(tmp3):
                nums.append(str(max(int(tmp1[0]), int(tmp3[0]))))
            else:
                nums.append(tmp1[0])
        else:
            tmp1 = re.findall(r'\d+', lines[i+1][cords-3:cords])
            tmp2 = re.findall(r'\d+', lines[i+1][cords+1:cords+4])
            if len(tmp1) > 0 and lines[i+1][cords-1].isdigit():
                nums.append(tmp1[-1])
            if len(tmp2) > 0 and lines[i+1][cords+1].isdigit():
                nums.append(tmp2[0])
        res1 = re.findall(r'\d+',lines[i][cords-3:cords])
        res2 = re.findall(r'\d+',lines[i][cords+1:cords+4])
        if len(res1)>0 and lines[i][cords-1].isdigit():
            nums.append(res1[-1])
        if len(res2)>0 and lines[i][cords+1].isdigit():
            nums.append(res2[0])
        if len(nums) == 2:
            sm += int(nums[0]) * int(nums[1])
print(sm)