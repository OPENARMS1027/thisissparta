import sys
import heapq
# sys.stdin = open("input.txt")


def find_max_time(start,end):
    heap = []
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        val, cur = heapq.heappop(heap)

        if cur == end:
            return dist[end]
        
        if dist[cur] < val:
            continue

        for next, next_val in dis[cur]:
            new_val = val + next_val

            if new_val < dist[next]:
                dist[next] = new_val
                heapq.heappush(heap,(new_val,next))
            
    return dist[end]


# 파티를 열고 다시 각각의 마을로 돌아와야 함
N, M, X = map(int,sys.stdin.readline().split()) # N명의 학생, X 마을(노드)에 모여서 파티, M개의 도로(간선)
dis = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,i = map(int,sys.stdin.readline().split())
    dis[s].append((e,i))

answer = 0

for num in range(1,N+1):
    go = find_max_time(num,X)
    back = find_max_time(X,num)
    total = go + back
    answer = max(answer,total)


print(answer)

"""
각 마을에서 -> 파티장, 파티장 -> 각 마을 복귀까지 가장 오래 걸리는 거리는 ?
노드와 간선의 가중치를 이용하기 때문에 다익스트라 사용.
또 "하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다."
때문에 "최소거리 중 가장 오래 걸리는 것"을 구하는 문제

가는길 + 오는길의 합이 가장 큰 경우가 최대.
각 지점에서 다익스트라 2번을 통해서 값을 구할 수 있음.


+++++
다익스트라 시간 복잡도 O(M logN) 
문제 해결은 가능했지만 더 개선이 가능함.

주어진 입력 안에 돌아오는 길도 포함되어 있다는 점을 이용해서 "역방향 그래프" 사용
정방향(그대로), 역방향(도로 방향만 반대로 저장)해서 출발점이 하나인 것을 이용함
즉, 단순히 탐색 방향을 바꿔서 하는 것 

"""