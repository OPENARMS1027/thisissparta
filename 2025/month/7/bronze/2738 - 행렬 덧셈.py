N,M = map(int,input().split())
lst_A = [list(map(int,input().split())) for _ in range(N)]
lst_B = [list(map(int,input().split())) for _ in range(N)]

for r in range(N):
    for c in range(M):
        lst_A[r][c] = lst_A[r][c]+ lst_B[r][c]
    print(*lst_A[r])
