from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while len(scoville) > 1:
        if scoville[0] >= K:
            break
            
        a = heappop(scoville)
        b = heappop(scoville)
        new_min_val = a + 2 * b
        heappush(scoville,new_min_val)
        answer += 1

    if scoville[0] < K:
        answer = -1
            
    return answer




"""
힙은 항상 최소합을 기준으로 하고 힙은 보통 heapify를 사용해서 힙을 만들어줘야 함(덱처럼, 라이브러리 사용)
from heapq import heapify, heappop, heappush
힙의 idx 0 은 항상 최솟값을 가리킴. But idx 1,2 는 최소값의 순서가 아니라 무작위임 주의!
heappop은 return값이 있다.
"""