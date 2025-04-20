import sys

sr, sc = map(int, sys.stdin.readline().split())
sr -=1
sc -=1
lst = [list(input()) for _ in range(10)]

row = [True] * 10 # True가 가능
col = [True] * 10

min_answer = float('inf')
for i in range(10):
    for j in range(10):
        if lst[i][j] == 'o':
            row[i] = False
            col[j] = False

# 현재 위치가 안전한 곳이면 이동 필요 x
if row[sr] and col[sc]:
    min_answer = 0

# 현재 위치가 안전하지 않다면
else:
    for i in range(10):
            for j in range(10):
                if row[i] and col[j]:
                    min_answer = min(min_answer,abs(sr-i)+abs(sc-j))

print(min_answer)

