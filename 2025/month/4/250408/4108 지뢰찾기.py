# 비어있는 칸 마다 주변에 지뢰가 몇개 있는지


while True:
    R,C = map(int,input().split())
    if R == 0 and C == 0:
        break
    bomb = [list(map(str,input())) for _ in range(R)]

    for r in range(R):
        for c in range(C):
            count = 0
            # 비어있는 칸이면
            if bomb[r][c] == '.':
                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr < R and 0<= nc < C and bomb[nr][nc] == '*':
                        count += 1
            # 위치에 개수 넣어주기
                bomb[r][c] = str(count)

    for i in range(R):
        print(''.join(bomb[i]))

                    

    




