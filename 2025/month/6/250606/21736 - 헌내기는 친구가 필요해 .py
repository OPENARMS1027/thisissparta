import sys
from collections import deque

def dfs(sr,sc):
    q = deque()
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1
    q.append((sr,sc))
    count = 0


    while q:
        r, c = q.popleft()
        
        if campus[r][c] == 'P':
            count += 1
        
        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr = r + dr
            nc = c + dc
            if 0<= nr < N and 0<= nc < M and visited[nr][nc] == 0 and campus[nr][nc] != 'X':
                q.append((nr,nc))
                visited[nr][nc] = 1

    
    if count == 0:
        return 'TT'
    
    else:
        return count 



N,M = map(int,sys.stdin.readline().split())

# O는 빈 공간, X는 벽, I는 도연이, P는 사람
campus = [sys.stdin.readline() for _ in range(N)]

yeon_r =0
yeon_c =0

for r in range(N):
    for c in range(M):
        if campus[r][c] == 'I':
             yeon_r = r
             yeon_c = c

answer = dfs(yeon_r,yeon_c)
print(answer)