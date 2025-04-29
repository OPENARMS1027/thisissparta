from collections import deque
def bfs(s,e):
    q = deque()
    visited = [0] * 100001
    q.append([s,0])
    visited[s] = 1

    while q:
        x, time = q.popleft()

        if x == e:
            return time

        for next_x in (x+1, x-1, 2* x):
            if 0<=next_x<=100000 and visited[next_x] == 0:
                visited[next_x] = 1
                q.append([next_x,time+1])


N,M =map(int,input().split())
print(bfs(N,M))