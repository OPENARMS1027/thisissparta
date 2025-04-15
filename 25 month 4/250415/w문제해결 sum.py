# import sys
# sys.stdin = open('input.txt','r')
for tc in range(1,11):
    T = int(input())

    nums = [list(map(int,input().split())) for _ in range(100)]
    max_sum = 0

    # r 합
    for i in range(100):
        r_sum = 0
        for j in range(100):
            r_sum += nums[j][i]
        max_sum = max(r_sum, max_sum)

    # c 합
    for i in range(100):
        c_sum = 0
        for j in range(100):
            c_sum += nums[i][j]
        max_sum = max(c_sum,max_sum)


    dr,dc = 1,1
    r,c = 0,0
    dia_max = 0
    reverse_dia_max = 0
    # 대각선 합 왼 -> 오
    while r<100:
        dia_max += nums[r][c]
        r = r+ dr
        c = c+ dc

    # 대각선 합 오 -> 왼
    r,c = 0,99
    dr, dc = 1, -1

    while r<100:
        reverse_dia_max += nums[r][c]
        r = r+ dr
        c = c+ dc

    max_sum = max(max_sum,dia_max,reverse_dia_max)

    print(f"#{T} {max_sum}")
