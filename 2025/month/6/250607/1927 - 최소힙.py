import heapq
import sys
sys.stdin = open('input.txt')


q = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            answer = heapq.heappop(q)
            print(answer)
    else:
        heapq.heappush(q,x)