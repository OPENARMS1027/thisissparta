import sys
sys.stdin = open("input.txt")


N = int(input())
schedules = []
check_box = [[False] * 365 for _ in range(N)]

for _ in range(N):
    s,e = map(int,input().split())
    schedules.append((s,e))

schedules.sort(key = lambda x: (x[0],-x[1]))


for s,e in schedules:
    hang = 0

    while check_box[hang][s] != False:
        hand += 1

    for idx in range(s,e+1):
        check_box[hang][idx] = True




