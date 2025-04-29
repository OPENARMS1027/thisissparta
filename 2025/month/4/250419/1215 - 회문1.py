for tc in range(1,11):
    N = int(input())

    full_count = 0
    pal = [list(input()) for _ in range(8)]
    # 열 확인
    for i in range(8):
        for j in range(N//2,8-N//2):
            count = 0
            for a in range(1,N//2+1):
                if pal[i][j-a] == pal[i][j+a]:
                    count += 1
            if count == N//2:
                full_count += 1


    # 행 확인
    for j in range(8):
        for i in range(N//2,8-N//2):
            count = 0
            for a in range(1,N//2+1):
                if pal[i-a][j] == pal[i+a][j]:
                    count += 1
            if count == N//2:
                full_count += 1



