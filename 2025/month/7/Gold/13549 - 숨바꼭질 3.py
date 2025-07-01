import sys
from collections import deque
# sys.stdin = open("input.txt")

def bfs(start,zero):
    q = deque()
    q.append((start,zero))
    visited = [False] * 100001
    visited[start] = True
    while q:
        now, count = q.popleft()
        
        if now == K:
            return count 
        
        next1 = now -1
        next2 = now +1
        next3 = now * 2

        if 0<= next3 < 100001 and not visited[next3]:
            visited[next3] = True
            q.appendleft((next3,count))

        
        if 0<= next1< 100001 and not visited[next1]:
            visited[next1] = True
            q.append((next1,count+1))
        if 0<= next2< 100001 and not visited[next2]:
            visited[next2] = True
            q.append((next2,count+1))

            

N, K = map(int,sys.stdin.readline().split())
answer = bfs(N,0)
print(answer)

"""
순간이동하는 경우 시간이 소요되지 않기 때문에 덱의 맨 앞에다가 넣어준다.
"""