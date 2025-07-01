import sys
from collections import deque
sys.stdin = open("input.txt")

def bfs(start,zero):
    q = deque()
    q.append((start,zero))
    
    while q:
        now, count = q.popleft()
        
        if now == K:
            return count 
        
        next1 = now -1
        next2 = now +1
        next3 = now * 2

        if now > K:
            q.append((next1,count+1))
        
        else:
            q.append((next2,count+1))
            q.append((next3,count))

            

N, K = map(int,sys.stdin.readline().split())
answer = bfs(N,0)
print(answer)