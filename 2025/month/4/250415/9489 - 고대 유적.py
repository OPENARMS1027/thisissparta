# import sys
# sys.stdin = open("input.txt","r")
T = int(input())
for tc in range(1,1+T):
    N,M = map(int,input().split())

    # r,c
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_length = 0
    # 길이 N개 배열 M줄개 
    for i in range(N):
        count = 0
        for j in range(M):
            if arr[i][j] == 1:
                count += 1
            elif arr[i][j] == 0:
                max_length = max(max_length,count)
                count = 0
        max_length = max(max_length,count)

    for i in range(M):
        count = 0 
        for j in range(N):
            if arr[j][i] == 1:
                count += 1
            elif arr[j][i] == 0:
                max_length = max(max_length,count)
                count = 0
        max_length = max(max_length,count)

    print(f"#{tc} {max_length}")