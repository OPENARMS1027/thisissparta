import sys
from collections import deque
sys.stdin = open("input.txt")

def bfs(start,count):
    q = deque()
    visited = [False] * 100 
    q.append((start,count))
    visited[start] = True
    
    while q:
        cur,count  = q.popleft()
        visited[cur] = True

        if cur == 99:
            return count 

        # 주사위 먼저 굴림
        for num in range(1,7):
            next_num = cur + num
            if next_num >= 100:
                continue

            if gogo[next_num]:
                next_num = gogo[next_num]

            if not visited[next_num]:
                visited[next_num] = True
                q.append((next_num,count + 1))
                

N,M = map(int,sys.stdin.readline().split())
gogo = [0] * 100  # 뱀, 사다리 위치 배열

for a in range(N):
    x,y = map(int,sys.stdin.readline().split())
    gogo[x-1]= y-1 

for b in range(M):
    x,y = map(int,sys.stdin.readline().split())
    gogo[x-1] = y-1

answer = bfs(0,0)
print(answer)


"""
## 주의점
1. 2차원 배열에 굳이 집착하지 않아도 됨. 1차원 배열로 풀리는 문제
2. 진행 과정을 명확하게 구분

## 틀린점
1. 만들어 준 배열 'gogo'의 경우 field기 때문에 1)그냥 이동하는 것 먼저 해준 뒤, 2)뱀, 사다리를 확인해줘야 한다.
!! 한번에 해주면 일반적으로 이동하는 경우를 고려하지 못 하게 됨.
"""