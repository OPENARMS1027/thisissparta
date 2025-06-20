"""
연결 요소: 서로 도달 가능한 정점들의 집합 
혼자 있어도 연결 요소가 된다
1 - 2,5
3 - 4,6
테케 첫번째는 이렇게 2개인거임
문제 풀이: 한 개의 정점에서 깊이 기준으로 탐색(DFS)하여 체크해준다.
한번 DFS가 실행될 때 마다 하나의 연결요소를 확인가능 함

"""
import sys
# sys.stdin = open("input.txt")

def dfs(two_ways,visited,i):
    visited[i] = True
    for num in two_ways[i]:
        if not visited[num]:
            dfs(two_ways,visited,num)



# 정점 개수 N개, 간선 개수 M개
N,M = map(int,sys.stdin.readline().split())
two_ways = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0
# 간선의 양 끝점 u와 v
for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    two_ways[u].append(v)
    two_ways[v].append(u)

for i in range(1,N+1):
    if not visited[i]:
        dfs(two_ways,visited,i)
        count += 1
# print(two_ways)  
# print(visited)
print(count)