T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split()) # 보드 한 변의 길이N, 돌의 놓는 횟수 M
    Go = [[0] * N for _ in range(N)]

    #초기 오셀로 값 할당
    Go[N//2-1][N//2-1] = 2
    Go[N//2-1][N//2] = 1
    Go[N//2][N//2-1] = 1
    Go[N//2][N//2] = 2

    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,-1),(1,1),(-1,-1)] # 상 하 좌 우 오른위 왼아래 오른아래 왼위
    # 보드 위 흑돌, 백돌 개수 출력하기기
    # M회 만큼 돌 위치 정보 받기
    for _ in range(M):
        input_c, input_r, color = map(int,input().split()) # row, column, 돌 색 받기(1이 흑돌, 2가 백돌)
        # 주어진 좌표는 x,y 기준이므로 반대로 할당해줌
        # 좌표가 1부터니까 idx 수정
        input_r -= 1
        input_c -= 1
        Go[input_r][input_c] = color
        # 놓은 곳 주변에 상대 편 돌이 있는지 체크한 후, 있다면 내 돌이 나올때까지 체크해서 빈 리스트에 추가
        for dr,dc in directions:
            nr =input_r+dr
            nc =input_c+dc
            have_to_flip = [] # 바꿔야할 돌 리스트 
            while 0<=nr<N and 0<=nc<N and Go[nr][nc] not in [0,color]: # 놓은곳 주변이 상대방 돌일 때 
                have_to_flip.append([nr,nc]) # 바꿔야 할 리스트에 추가
                nr += dr # 한 방향으로 쭉 탐색
                nc += dc # 한 방향으로 쭉 탐색
            # while문에서 나온 좌표는 color 거나 0인데 color라면 사이에 있는 것들 바꿔줘야 함   
            if 0<=nr<N and 0<=nc<N and Go[nr][nc] == color:
                for fr,fc in have_to_flip:
                    Go[fr][fc] = color
    
    # 마지막으로 완료된 바둑판에서 세주기
        
    count_black = 0 # 흑돌 세줄 변수 할당
    count_white = 0 # 백돌 세줄 변수 할당

    for i in range(N):
        for j in range(N):
            if Go[i][j] == 1: # 흑돌일 때
                count_black +=1 # 카운트해주기
            elif Go[i][j] == 2: # 백돌일 때
                count_white +=1 # 카운트해주기

    print(f"#{tc} {count_black} {count_white}")