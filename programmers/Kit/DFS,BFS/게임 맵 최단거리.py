from collections import deque
def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
     
    def bfs(sr,sc):
        q = deque()
        q.append((sr,sc))
        visited = [[0] * m for _ in range(n)]
        visited[sr][sc] = 1
        
        while q:
            cur_r, cur_c = q.popleft()
            
            if cur_r == n-1 and cur_c == m-1:
                result = visited[cur_r][cur_c]
                return result 
            
            for dr,dc in ((0,1),(1,0),(0,-1),(-1,0)):
                nr = cur_r + dr
                nc = cur_c + dc
                if 0<=nr<n and 0<= nc < m and visited[nr][nc] == 0 and maps[nr][nc] != 0:
                    q.append((nr,nc))
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
        return -1

    answer = bfs(0,0)
    return answer


"""
BFS 정리
1. 최단거리 구할 때 큐를 사용해서 쌓여진대로 뽑아서 주위 탐색
"""