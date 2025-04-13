import sys
sys.setrecursionlimit(10**6) # 백준 자체에 재귀 제한이 1000까지라 코드 작성으로 늘려줄 수 있음
# sys.stdin = open("input.txt",'r')
def recur(x,y):
    for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
        nx = x +dx
        ny = y +dy
        if 0<=nx< N and 0<=ny < M:
            if bachu[nx][ny] == 0 or bachu[nx][ny] ==9:
                continue
            elif bachu[nx][ny] == 1:
                bachu[nx][ny] = 9
                recur(nx,ny)
    return 
T = int(input())

for tc in range(1,1+T):
    M, N, K = map(int,input().split()) # 배추밭 가로길이 M, 세로길이 N, 배추가 심어져 있는 위치의 개수 K
    # c가 M까지 , r이 N까지
    bachu = [[0] * M for _ in range(N)] # 배추밭 
    count = 0
    for i in range(K):
        x, y = map(int,input().split())
        bachu[y][x] = 1 # 배추 있는 곳 1 넣어주기
    

    for r in range(N):
        for c in range(M):
            if bachu[r][c] == 1:
                bachu[r][c] = 9
                recur(r,c)
                count += 1
                    
                        
    print(count)

    

    
