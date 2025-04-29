T = int(input())
for tc in range(1,1+T):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    monster_i = 0
    monster_j = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                monster_i = i
                monster_j = j

    for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
        for a in range(1,N):
            ni = monster_i +di*a
            nj = monster_j +dj*a
            if 0<=ni< N and 0<= nj <N:
                if board[ni][nj] == 1:
                    break
                board[ni][nj] = 9
    count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                count += 1
    print(f"#{tc} {count}")

