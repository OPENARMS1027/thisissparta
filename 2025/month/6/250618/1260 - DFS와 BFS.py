import sys 
from collections import deque
# sys.stdin=open("input.txt")
def dfs(start,visited,result):
    visited[start] = 1
    result.append(start)
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(next_node,visited,result)

def bfs(start):
    q=deque()
    visited = [0] * (N+1)
    q.append(start)
    visited[start] = 1
    result = []

    while q:
        c_node = q.popleft()
        result.append(c_node)

        for n_node in graph[c_node]:           
            if visited[n_node] ==0:
                visited[n_node] = 1
                q.append(n_node)
    return result

N,M,V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

# print(graph)
visited_dfs = [0] * (N+1)
result_dfs = []
for _ in range(M):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for c_node in graph:
    c_node.sort()

dfs(V,visited_dfs,result_dfs)
print(*result_dfs)

result_bfs = bfs(V)
print(*result_bfs)