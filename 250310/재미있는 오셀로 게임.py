T = int(input())

for testcase in range(1,1+T):
    N, M = map(int,input().split()) # 보드 한 변의 길이N, 돌의 놓는 횟수 M
    Go = [[0] * N for _ in range(N)]


    #초기 오셀로 값 할당
    Go[N//2-1][N//2-1] = 2
    Go[N//2-1][N//2] = 1
    Go[N//2][N//2-1] = 1
    Go[N//2][N//2] = 2

    directions = [(-1,0),(1,0),(0,-1),(0,-1),(-1,1),(1,-1),(1,1),(-1,-1)] # 상 하 좌 우 오른위 왼아래 오른아래 왼위
    # 보드 위 흑돌, 백돌 개수 출력하기기
    # M회 만큼 돌 위치 정보 받기
    for _ in range(M):
        input_c, input_r, color = map(int,input().split()) # row, column, 돌 색 받기(1이 흑돌, 2가 백돌)

        # # 돌 위치 받아서 놓고 그 때마다 바꿔야할 돌 있는지 확인해보기
        # # 인덱스 수정해줘야 함
        #
        #
        # r = input_r -1 # 현재 좌표 r값
        # c = input_c - 1 # 현재 좌표 c값
        # Go[r][c] = color
        # # 세로,가로 대각선 확인 ?
        #
        # # 상, 하, 좌, 우 확인하기
        # for dr, dc in directions:
        #     nr,nc = r + dr, c + dc
        #
        #



    count_black = 0 # 세 줄 변수 할당
    count_white = 0 # 세 줄 변수 할당

    for i in range(N):
        for j in range(N):
            if Go[i][j] == 1: # 흑돌일 때
                count_black +=1
            elif Go[i][j] == 2: # 백돌일 때
                count_white +=1

    print(f"#{testcase} {count_black} {count_white}")