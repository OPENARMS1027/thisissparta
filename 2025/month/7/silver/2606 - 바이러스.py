import sys
# sys.stdin = open("input.txt")
from collections import deque

def bfs(sc):
    q = deque()
    q.append(sc)
    visited = [False] * N 
    visited[sc] = True
    count = 0

    while q:
        com= q.popleft()
        
        for n_com in check[com]:
            if not visited[n_com]:
                q.append(n_com)
                visited[n_com] = True
                count += 1   

    return count 

N = int(sys.stdin.readline())
S = int(sys.stdin.readline())
check = [[] for _ in range(N)]

for _ in range(S):
    A,B = map(int,sys.stdin.readline().split())
    check[A-1].append(B-1) 
    check[B-1].append(A-1)
# print(check)
answer = bfs(0) 
print(answer)