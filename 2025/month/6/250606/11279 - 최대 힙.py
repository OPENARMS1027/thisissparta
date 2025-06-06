import sys
import heapq

# sys.stdin = open('input.txt')
q = []

N =int(sys.stdin.readline())

for _ in range(N):
    x = int(sys.stdin.readline())
    
    # 가장 큰 값 출력 후 배열에서 제거
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            answer = heapq.heappop(q)
            print(-answer)
    
    else:
        heapq.heappush(q,-x)