from heapq import heappush, heappop
from collections import defaultdict

def solution(operations):
    min_heap = []
    max_heap = []
    count = defaultdict(int)

    def clean_min():
        while min_heap and count[min_heap[0]] == 0:
            heappop(min_heap)

    def clean_max():
        while max_heap and count[-max_heap[0]] == 0:
            heappop(max_heap)

    for op in operations:
        if op[0] == 'I':
            x = int(op[2:])
            heappush(min_heap, x)
            heappush(max_heap, -x)
            count[x] += 1

        else:  # 'D'
            if op == 'D 1':
                clean_max()
                if max_heap:
                    x = -heappop(max_heap)
                    count[x] -= 1

            elif op == 'D -1':
                clean_min()
                if min_heap:
                    x = heappop(min_heap)
                    count[x] -= 1

    clean_min()
    clean_max()

    if not min_heap or not max_heap:
        return [0, 0]

    return [-max_heap[0], min_heap[0]]



"""
이중우선순위큐 -> 힙을 2개 써서 최솟갑, 최댓값을 따로 관리
But 값을 둘다 뺴줘야 하는데 그게 힙 특성 상 안됨(최솟값 혹은 최댓값(음의 값))
따라서 값을 빼준지 확인할 자료구조가 필요 -> 딕셔너리

이제 최솟값, 최댓값을 빼줄 때 현재의 최솟값, 최댓값이 빠진건지 아닌지 딕셔너리를 통해 확인 
함수로 빼는건 선택.
계속해서 빼준 것을 확인하다가 그냥 값인게 나오면은 반복문을 빠져나와서 최댓값이나 최솟값을
빼주는 구조임!!!!!!!! 다시 풀자 그냥 

"""

