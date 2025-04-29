from collections import deque
# import sys
# sys.stdin = open("input.txt","r")

def bfs():
    q = deque()
    q.append((1,1))
    visited = [[0] * 16 for _ in range(16)]
    visited[1][1] = 1

    while q:
        r,c = q.popleft()
        

        if maze[r][c] == 3:
            return 1
        
        for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
            nr = r + dr
            nc = c + dc
            if 0<=nr<=15 and 0<=nc<=15:
                if (maze[nr][nc] == 0 or maze[nr][nc] == 3) and visited[nr][nc] == 0:
                    q.append((nr,nc))
                    visited[nr][nc] = 1
    return 0
                    
    

for i in range(1,11):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    # x,y 방향 col , row
    # 시작점 1,1
    # 도착점 13,13 
    answer = bfs()
    print(f"#{i} {answer}")
