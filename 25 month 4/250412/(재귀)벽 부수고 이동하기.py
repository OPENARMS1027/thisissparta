import sys
sys.setrecursionlimit(10**6)  # 깊이 제한 증가

N, M = map(int, input().split())
map = [list(map(int, input())) for _ in range(N)]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
min_count = float('inf')  # 최솟값 초기화

def dfs(r, c, count, break_check):
    global min_count

    if r == N - 1 and c == M - 1:
        min_count = min(min_count, count)
        return

    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < M:
            if map[nr][nc] == 0 and not visited[nr][nc][break_check]:
                visited[nr][nc][break_check] = True
                dfs(nr, nc, count + 1, break_check)
                visited[nr][nc][break_check] = False  # 백트래킹

            elif map[nr][nc] == 1 and break_check == 0 and not visited[nr][nc][1]:
                visited[nr][nc][1] = True
                dfs(nr, nc, count + 1, 1)
                visited[nr][nc][1] = False  # 백트래킹

# 시작점 방문 체크
visited[0][0][0] = True
dfs(0, 0, 1, 0)

print(min_count if min_count != float('inf') else -1)
