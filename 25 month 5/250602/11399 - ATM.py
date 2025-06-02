import sys

N = int(sys.stdin.readline())
order = list(map(int,sys.stdin.readline().split()))
order.sort()

answer = 0
a = 0
for num in (order):
    a += num
    answer += a

print(answer)


