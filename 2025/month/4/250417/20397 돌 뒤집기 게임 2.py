# import sys
# sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,1+T):
    N,M = map(int,input().split())
    rocks = list(map(int,input().split()))

    for _ in range(M):
        i,j = map(int,input().split())
        i = i -1
        
        for a in range(1,j+1):
            if 0<=i-a and i+a < N:
                if rocks[i+a] == rocks[i-a]:
                    if rocks[i+a] == 1:
                        rocks[i+a] = 0
                        rocks[i-a] = 0
                    else:
                        rocks[i+a] = 1
                        rocks[i-a] = 1
    print(f"#{tc}",*rocks)