# import sys
# sys.stdin = open('input.txt','r')

for tc in range(1,11):
    T= int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    start_row = ladder[99].index(2)


    r = 99
    c = start_row
    dr = [-1,0,0]
    dc = [0,-1,1]

    while r > 0:
        if 0<=r+dr[1] <100 and 0<=c+dc[1]<100 and ladder[r+dr[1]][c+dc[1]]:
            r = r +dr[1]
            c = c +dc[1]
            ladder[r][c] = 0

        elif 0<=r+dr[2] <100 and 0<=c+dc[2]<100 and ladder[r+dr[2]][c+dc[2]]:
            r = r +dr[2]
            c = c +dc[2]
            ladder[r][c] = 0

        elif 0<=r+dr[0] <100 and 0<=c+dc[0]<100 and ladder[r+dr[0]][c+dc[0]]:
            r = r+dr[0]
            c = c+dc[0]
            ladder[r][c] = 0

    print(f"#{T} {c}")

