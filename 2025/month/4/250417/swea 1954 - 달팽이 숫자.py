T = int(input())
for tc in range(1,1+T):
    N = int(input())

    snail = [[0] * N for _ in range(N)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0] # 우 하 좌 상
    idx = 1 # 인덱스

    dir = 0
    r = c = 0
    snail[r][c] = idx

    while idx < N*N:

        nr = r+ dr[dir]
        nc = c+ dc[dir]

        # 범위 내이고 가지 않을 곳일 때
        if 0<=nr<N and 0<=nc<N and snail[nr][nc] == 0:
            idx += 1
            snail[nr][nc] = idx
            r,c = nr, nc


        else:
            dir = (dir + 1) % 4
    
    print(f"#{tc}")
    for row in snail:
        print(*row)


