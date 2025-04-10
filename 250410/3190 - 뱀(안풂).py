from collections import deque
def snake_road():
    visited = [[0]* N for _ in range(N)]
    q = deque()
    q.append((0,0)) # r, c, time
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    turn_idx = time = 0
    i = j = 0
    while True:
        # 종료 조건
        if i < 0 or j < 0 or i >= N or j >= N or board[i][j] == 9:
            return time

        # 사과 체크 후 꼬리 변경
        if time >= 1:
            if board[i][j] == 0:
                a, b = q.popleft()
                board[a][b] = 0

        # 이동하기 전 시간 먼저 체크
        if time in turn_time:
            if turn_time[time] == 'L':  # 왼쪽이면
                turn_idx -= 1
                # if abs(turn_idx) <= -4:
                #     turn_idx = turn_idx % 4

            elif turn_time[time] == 'D':  # 오른쪽이면
                turn_idx += 1
                # if abs(turn_idx) >= 4:
                #     turn_idx = turn_idx % 4
            turn_idx = abs(turn_idx % 4)

        # 방문 체크
        q.append((i,j))
        board[i][j] = 9
        i, j = i + di[turn_idx], j + dj[turn_idx]  # 다음 갈 위치
        time += 1


N = int(input()) # 보드 길이
K = int(input()) # 사과의 개수 
board = [[0]*N for _ in range(N)]
for i in range(K):
    a, b = map(int,input().split())
    board[a-1][b-1] = 1 # 사과 체크

L = int(input()) # 뱀 방향 변환 횟수
turn_time = {} # 방향전환 값 받아줄 딕셔너리
for i in range(L):
    # x초가 끝난 뒤에 왼쪽(L) 또는 오른쪽(D)으로 90도 방향 회전
    x, c = map(str,input().split())
    turn_time[int(x)] = c # 딕셔너리 추가

print(snake_road())