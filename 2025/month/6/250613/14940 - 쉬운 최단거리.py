import sys
from collections import deque

# sys.stdin = open("input.txt")
# 갈 수 있는 곳 체크
def bfs(sr,sc):
    q = deque()
    q.append((sr,sc))
    visited[sr][sc] = 0

    while q:
        r,c = q.popleft()
        
        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr = r + dr
            nc = c + dc
            if 0<=nr<n and 0<=nc<m and visited[nr][nc] == -1 and field[nr][nc] != 0:
                q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
            elif 0<=nr<n and 0<=nc<m and field[nr][nc] == 0:
                visited[nr][nc] = 0

# 도달하지 못 하는곳 중 원래 갈 수 없는 땅 체크
def check_cant_go():
    for r in range(n):
        for c in range(m):
            # 시작점 아닌 거 중에
            if field[r][c] != 2:
                if field[r][c] == 0:
                    visited[r][c] = 0
                

                

n,m = map(int,sys.stdin.readline().split())
field = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# print(field)
visited = [[-1] * m for _ in range(n)]

for r in range(n):
    for c in range(m):
        if field[r][c] == 2:
            bfs(r,c)

check_cant_go()
for a in range(n):
    print(*visited[a])
