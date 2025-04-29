import sys
K = int(sys.stdin.readline())
# 4가지 경우의 참외밭

max_length = float('-inf')
length = []
direction = []
for i in range(6):
    # 변의 방향과 길이
    # 동 1 서 2 남 3 북 4
    a, b = map(int,input().split())
    direction.append(a)
    length.append(b)

for i in range(6):
    # 동,서
    if direction[i] == 1 or direction[i] == 2:
        if length[i] > max

    