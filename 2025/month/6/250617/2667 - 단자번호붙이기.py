import sys
from collections import deque

# 방문한거는 9
# 집이 있을 때마다 bfs 돌려서 그 주변 모두 방문 체크
def bfs(sr,sc,lst):
    global count
    each_count = 1
    q = deque()
    q.append((sr,sc))
    lst[sr][sc] = 9
    
    while q:
        r,c  = q.popleft()
        
        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr = r + dr
            nc = c + dc
            if 0<= nr < N and 0<= nc <N and complexes[nr][nc] == 1 and lst[nr][nc] != 9:
                lst[nr][nc] = 9
                q.append((nr,nc))
                each_count += 1 
    return each_count
       


# 총 단지수 출력
# sys.stdin = open("input.txt")
N = int(sys.stdin.readline())
complexes = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)] # 문자열

visited = [[0] * N for _ in range(N)]
count_lst = []
# print(complexes)
count = 0 # 총 단지수
for r in range(N):
    for c in range(N):
        if complexes[r][c] == 1 and visited[r][c] !=9:
            count += 1
            in_count = bfs(r,c,visited)
            count_lst.append(in_count)
count_lst.sort()

print(count)
for num in count_lst:
    print(num)


