import sys,copy
from collections import deque

# 조합 찾기
def backtracking():
    global general_zone
    for a in range(N):
        for b in range(M):
            if map[a][b] == 0:
                general_zone.append((a,b))


# 조합 별 벽 만들 3개 뽑기
def choose_wall(start):
    global map,max_safezone
    if len(you_wall) == 3:
        # 뽑힐 때마다 안전 영역 구해서 최대값 갱신하기
        copy_map = copy.deepcopy(map)

        # 조합나온거 벽으로 바꿔주기
        for a in range(3):
            x,y = you_wall[a]
            copy_map[x][y] = 1

        # 바이러스 분출 후 안전 영역 구하기
        safe_count = find_safezone(copy_map)

        # 최대값 갱신
        if max_safezone < safe_count:
            max_safezone = safe_count

        return 
    
    for i in range(start,len(general_zone)):
        you_wall.append(general_zone[i])
        choose_wall(i+1)
        you_wall.pop()



# 바이러스 분출 후 안전 영역 구하기
def find_safezone(copy):
    count = 0
    for a in range(N):
        for b in range(M):
            if copy[a][b] == 2:
                q = deque()
                q.append((a,b))
                visited = [[0] * M for _ in range(N)]
                visited[a][b] = 1
                while q:
                    r, c = q.popleft()
                    for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                        nr = r + dr
                        nc = c + dc
                        if 0<=nr <N and 0<= nc < M and copy[nr][nc] == 0 and visited[nr][nc] == 0:
                            copy[nr][nc] = 2
                            visited[nr][nc] = 1
                            q.append((nr,nc))
    for i in range(N):
        for j in range(M):
            if copy[i][j] == 0:
                count += 1
    return count      

# sys.stdin = open("input.txt","r")
N,M = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
general_zone = [] # 벽 만들기 가능한 곳 조합
you_wall = [] # 벽으로 만들 곳 
max_safezone = -1
backtracking()
choose_wall(0)
print(max_safezone)
