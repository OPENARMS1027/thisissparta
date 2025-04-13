from collections import deque
import sys
sys.stdin = open('input.txt','r')
'''
터널 구조물 type
1 - 상하좌우
2 - 상,하
3 - 좌, 우
4 - 상, 우
5 - 하, 우
6 - 하, 좌
7 - 상, 좌

탈주범이 위치할 수 있는 장소의 개수 계산
'''

def bfs(i,j):
    q = deque()
    visited = [[0] * M for _ in range(N)] # 도둑 존재 가능 체크
    q.append((i,j,turnel[i][j]))
    visited[i][j] = 1
    # dr = [-1,1,0,0] # 상 하 좌 우
    # dc = [0,0,-1,1]

    delta = {1:[(-1,0),(1,0),(0,-1),(0,1)],
              2: [(-1,0),(1,0)],
              3: [(0,-1),(0,1)],
              4: [(-1,0),(0,1)],
              5: [(1,0),(0,1)],
              6: [(1,0),(0,-1)],
              7: [(-1,0),(0,-1)]
              }
    
    while q:
        r, c, hole  = q.popleft()

        for dr,dc in delta[hole]:
            nr = r + dr
            nc = c + dc

            if 0<= nr < N and 0<= nc < M:
                if visited[nr][nc] != 0:
                    continue
                value = turnel[nr][nc]
                if value != 0 and (-dr,-dc) in delta[value]:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr,nc,value))

    count = 0
    for i in range(N):
        for j in range(M):
            if 0< visited[i][j] <=L:
                count += 1
    return count

T = int(input())

for tc in range(1,1+T):
    # r,c 순서로
    # N,M 터널 세로 N,가로 M 
    # R,C 맨홀 세로 R,가로 C
    # 탈출에 소요된 시간 L
    N,M,R,C,L = map(int,input().split())

    # 지하 터널 지도 정보
    turnel = [list(map(int,input().split())) for _ in range(N)]
    answer = bfs(R,C)
    print(f"#{tc} {answer}")