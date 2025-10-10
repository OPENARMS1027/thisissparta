import sys
from collections import deque
sys.stdin = open("input.txt")

def bfs(start):
    q = deque()
    visited = [False] * 100 
    q.append(start)
    visited[start] = True
    count = 0
    
    while q:
        cur = q.popleft()
        visited[cur] = True

        # 주사위 먼저 굴림
        for num in range(1,7):
            cur += num
            visited[cur]

        if not visited[cur]:
        # 빈칸이 아닐 때
            if gogo[cur]:
                n_cur = gogo[cur]
                count += 1
                q.append(n_cur)

            # 빈칸일 때(주사위 따라)
            else:
                



N,M = map(int,sys.stdin.readline().split())
gogo = []  # 뱀, 사다리 위치 배열


for a in range(N):
    x,y = map(int,sys.stdin.readline().split())
    gogo.append((x,y))

for b in range(M):
    x,y = map(int,sys.stdin.readline().split())
    gogo.append((x,y))

print(gogo)
