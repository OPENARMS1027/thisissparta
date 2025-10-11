import sys
import heapq
# sys.stdin = open("input.txt")


def dijkstra(start):
    q = []
    dis_visit = [float('inf')] * (V+1)
    dis_visit[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist,cur = heapq.heappop(q)

        if dis_visit[cur] < dist:
            continue 

        for next, value in graph[cur]:
            new_dist = dist + value 

            if new_dist < dis_visit[next]:
                dis_visit[next] = new_dist
                heapq.heappush(q,(new_dist,next))
        

    return dis_visit


# 정점 개수 V, 간선 개수 E
V, E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))

ans_list = dijkstra(K)

for num in range(1,V+1):
    if ans_list[num] == float('inf'):
        print('INF')
    else:
        print(ans_list[num])


"""
다익스트라는 모든 경로를 다 확인하면서
가중치 배열에 계속해서 최소값을 갱신하는 로직

dist는 현재 노드(cur)까지 오는 데 걸린 총 거리
현재 위치에서 최소인 부분을 확인하는 과정인거임

## 주의할 점
1. 인접그래프를 이용할 때는 일반적으로 (다음 노드,가중치)의 형태로
2차원 그래프에 append해주는 형식
최소 힙을 이용할 때는 앞 원소를 우선해서 고려하기 때문에
가중치를 앞에 넣어서 push해준다.


2. 비교를 굳이 2번 해줘야 하는가 ?, 
전에 있던 거리vs새로 계산된 거리 비교라 같은 것이 아닌가?

ㄴㄴ아님. 
위쪽 if문 비교 조건 - 내가 넣어준 가능성 있는 모든 경로 중
최신 거리 정보인지 확인하는 것
"지금 꺼낸 이 경로는 이미 더 짧은 걸로 갱신됐으니 패스"
즉, 유효성 검사

아래쪽 if문 비교 조건 - 현재 노드에서 다음 노드로 이동하며
새로 계산된 거리가 기존 최단거리보다 짧은지 확인
위에서 말한 가능성 있는 경로들 다 넣어주는 과정
"이 길은 새로운 더 좋은 경로니까 저장해둬야지"
즉, 최단거리 갱신 판단

"""