import sys
from collections import deque
# sys.stdin = open("input.txt")

def find_tomato(tr,tc):
    day_count = 0
    q = deque()
    q.append((tr,tc))
    tomato[tr][tc] == 1

    while q:
        count_check = 0
        r, c = q.popleft()

        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr = r + dr
            nc = c + dc
            if 0<=nr < N and 0<=nc < M and tomato[nr][nc] == 0:
                count_check +=1
                tomato[nr][nc] = 1
                q.append((nr,nc))

        if count_check != 0: # 바꾼게 있으면 
            day_count += 1 # 날짜 수 세기

    return day_count

M,N =map(int,sys.stdin.readline().split())
tomato = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result = 0
answer = 0
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            full_day = find_tomato(r,c)
            result = max(result,full_day) # 익은거 기준으로 주변에 안 익은게 없으면 +0, 익을게 있어서 쭉 익게 했으면 +1


# 안 익은거 있는지 확인
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 0:
            answer = -1 

# 안 익은게 있다면 
if answer == -1:
    print(-1)
else:
    print(result)