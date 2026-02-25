# import sys
from collections import deque
# sys.stdin = open("input.txt")

N = int(input())
r1,c1,r2,c2 = map(int,input().split())

def bfs(sr,sc,er,ec):
    max_cnt = 0
    q = deque()
    visited = [[False] * N for _ in range(N)]
    q.append((sr,sc,0))
    visited[sr][sc] = True

    while q:
        cur_r,cur_c,cur_cnt = q.popleft()
        if (cur_r,cur_c) == (er,ec):
            max_cnt = max(max_cnt, cur_cnt)
            return max_cnt
        
        for dr,dc in ((2,1),(2,-1),(0,-2),(0,2),(-2,1),(-2,-1)):
            nr = cur_r + dr
            nc = cur_c + dc
            if 0<= nr < N and 0<= nc < N and not visited[nr][nc]:
                q.append((nr,nc,cur_cnt+1))
                visited[nr][nc] = True
    
    return -1
answer = bfs(r1,c1,r2,c2)
print(answer) 
