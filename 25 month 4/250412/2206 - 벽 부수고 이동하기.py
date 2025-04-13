from collections import deque 
def find_way():
    q = deque()
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)] # 방문체크 - 
    q.append((0,0,0,False)) # r,c,count,break_point
    visited[0][0][0] = True

    while q:
        cur_r, cur_c, count,break_point = q.popleft()

        if cur_r == N-1 and cur_c == M-1:
            count += 1
            return count 
        
        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr = cur_r + dr
            nc = cur_c + dc
            if nr<0 or nr>= N or nc<0 or nc>=N:
                continue
            if 0<=nr<N and 0<=nc<M:
                if map[nr][nc] == 0 and not visited[nr][nc][break_point]:
                    visited[nr][nc][0] = True
                    q.append((nr,nc,count+1,break_point))
                    
                elif map[nr][nc] == 1 and break_point == False and not visited[nr][nc][1] :
                    visited[nr][nc][1] = True
                    q.append((nr,nc,count+1,1))
    
    return -1
                    
## 이해 안 가는 부분 : 왜 True False 로 인자를 append 해주지 않고 굳이 변수를 사용해서 넘겨주는건지                 
# 3차원 배열의 [r][c][0]의 경우 벽 부수지 않은 방문 체크, [r][c][1]의 경우 벽 부순 방문 체크
N,M =map(int,input().split())
map = [list(map(int,input())) for _ in range(N)]
# 0,0과 N-1,M-1은 항상 0
answer = find_way()
print(answer)


# 메모리 초과 발생
# 방문 배열을 2차원 배열 2개로 만들어 준다


'''
from collections import deque

def find_way():
    q = deque()

    # visited 배열을 벽 안 부셨을 때와 부셨을 때로 나누어서 2차원 배열 2개로 관리
    visited_no_break = [[False] * M for _ in range(N)]  # 벽 안 부쉈을 때
    visited_break = [[False] * M for _ in range(N)]  # 벽 부쉈을 때

    # 시작점: (0,0), 거리 1, 벽 안 부셈 상태(0), 방문 체크
    q.append((0, 0, 1, False))
    visited_no_break[0][0] = True

    while q:
        r, c, dist, break_point = q.popleft()

        # 목적지에 도달한 경우
        if r == N - 1 and c == M - 1:
            return dist

        # 상하좌우 네 방향 탐색
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr = r + dr
            nc = c + dc

            # 범위 내에 있고, 이동 가능한 칸일 때
            if 0 <= nr < N and 0 <= nc < M:
                
                # 벽을 부수지 않은 상태에서 이동
                if map[nr][nc] == 0 and not break_point and not visited_no_break[nr][nc]:
                    visited_no_break[nr][nc] = True
                    q.append((nr, nc, dist + 1, break_point))

                # 벽을 부수고 이동
                elif map[nr][nc] == 1 and not break_point and not visited_break[nr][nc]:
                    visited_break[nr][nc] = True
                    q.append((nr, nc, dist + 1, True))

                # 벽을 이미 부순 상태에서 이동
                elif map[nr][nc] == 0 and break_point and not visited_break[nr][nc]:
                    visited_break[nr][nc] = True
                    q.append((nr, nc, dist + 1, True))

    # 도달할 수 없으면 -1 반환
    return -1

# 입력 처리
N, M = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(N)]

# 결과 출력
print(find_way())

'''