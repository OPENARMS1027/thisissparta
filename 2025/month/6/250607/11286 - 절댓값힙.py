import sys
import heapq
# sys.stdin = open('input.txt')
q = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            answer = heapq.heappop(q)[1]
            print(answer)
    else:
        heapq.heappush(q,(abs(x),x))