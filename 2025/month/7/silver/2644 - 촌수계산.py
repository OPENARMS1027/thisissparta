"""
아버지 형제 - 나 는 3촌임, 직계는 한 줄로 보고 
직계가 아니라면 올라가서 내려가야하는 듯 
"""

from collections import deque
import sys
sys.stdin = open("input.txt")

def chonsu(s,e):
    if s>e:
        s,e = e,s
    count = 0
    q=deque()
    visited = [False] * (n+1)
    q.append(s)
    visited[s] = True

    while q:
        node = q.popleft()
        
        if node == e:
            return count 

        for n_node in family[node]:
            visited[n_node] = True
            q.append(n_node)
            count += 1
            
    if count == 0:
        return


n = int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().split())
a -=1
b -=1 
m = int(sys.stdin.readline())


family = [[] for _ in range(n+1)]
for _ in range(m):
    # 부모, 자식 = x,y
    x,y = map(int,sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)
    