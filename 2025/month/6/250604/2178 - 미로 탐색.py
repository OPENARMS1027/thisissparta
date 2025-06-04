import sys
from collections import deque

def gogo(sr,sc):
    q = deque()
    q.append((sr,sc))
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1

    while q:
        r,c = q.popleft()

        if (r,c) == (N-1,M-1):
            return visited[N-1][M-1]
        
        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr = r + dr
            nc = c + dc
            if 0<=nr<N and 0<=nc<M and maze[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr,nc))

    





N,M = map(int,sys.stdin.readline().split())
maze = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
answer = gogo(0,0)
print(answer)