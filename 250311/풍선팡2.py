T = int(input())

for tc in range(1,1+T):
    N,M = map(int,input().split()) # N X M 크기의 격자판
    balloons = [list(map(int,input().split())) for _ in range(N)] # 2차원리스트 input

    max_flowers = 0 # 최대값 꽃가루 수

    # 풍선팡 2의 경우 그냥 상하좌우의 풍선이 추가로 터지는 것
    for r in range(N):
        for c in range(M):
            each_flowers_sum = 0 # 좌표별 값 추가해줄 변수 설정
            each_flowers_sum += balloons[r][c] # 중간 값 더해주기
            for dr, dc in ([0,1],[1,0],[0,-1],[-1,0]): # 델타 탐색
                nr = r + dr # 주변 좌표 할당
                nc = c + dc # 주변 좌표 할당
                if 0 <= nr <N and 0 <= nc <M: # 2차원 배열 안에 있다면
                    each_flowers_sum += balloons[nr][nc] # 해당값 추가

            if max_flowers < each_flowers_sum: # 최대값 최신화 좌표의 주변값이 더 크면
                max_flowers =each_flowers_sum  # 최신화

    print(f"#{tc} {max_flowers}")                            
             
