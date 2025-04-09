from collections import deque
def snake_road(s):
    visited = [[0]* N for _ in range(N)]
    q = deque()
    q.append((0,0,1)) # r, c, time
    visited[0][0] = 9 # 뱀 몸이 있는 곳은 9로 표시 

    di = []
    dj = []
    while q:
        i,j,time = q.popleft()
        if i < 0 or j <0 or i >= N or j >= N or visited[i][j] == 9:
            return time
        # 방향 바꿔줄 시간일 때
        if time == int(x):
            if c == 'L':
                if (i,j) == (-1,0):

                elif
                for di,dj in ()
            elif c == 'D':
                pass
        # 일반적일 때
        else:




N = int(input()) # 보드 길이
K = int(input()) # 사과의 개수 
board = [[0]*N for _ in range(N)]
for i in range(K):
    a, b = map(int,input())
    board[a-1][b-1] = 1 # 사과 체크
L = int(input()) # 뱀 방향 변환 횟수

for i in range(L):
    # x초가 끝난 뒤에 왼쪽(L) 또는 오른쪽(D)으로 90도 방향 회전
    x, c = map(str,input().split())
    

## 어떻게 방향바꿀때 확인하지?
## 왼쪽 오른쪽 정해졌고 바꿀때 델타를 어떻게 정해주지 ?



