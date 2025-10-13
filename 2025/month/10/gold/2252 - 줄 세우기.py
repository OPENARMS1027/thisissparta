import sys
from collections import deque
# sys.stdin = open("input.txt")


def stand_in_line(graph):
    global indegree
    q = deque()
    answer = []
    
    for i in range(1, len(graph)):
        if not indegree[i]:
            q.append(i)

    ## 이 부분 복습 및 유의
    while q:
        cur = q.popleft()
        answer.append(cur)

        for next in graph[cur]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    return answer
# N명, M번의 키 비교 횟수
N,M = map(int,sys.stdin.readline().split())

graph = [[] * (N+1) for _ in range(N+1)] # 
indegree = [0] * (N+1) # 진입차수 배열

for _ in range(M):
    A,B = map(int,sys.stdin.readline().split()) # A가 B 앞에 섬
    graph[A].append(B) # B앞에 A가 있음
    indegree[B] += 1

answer = stand_in_line(graph)
print(*answer)

"""
진입차수는 따로 관리해준다.

위상 정렬의 핵심 배열 2개
1. 각 노드의 다음 노드를 가리키는 배열(graph)
2. 진입차수 배열(indegree)


"""

