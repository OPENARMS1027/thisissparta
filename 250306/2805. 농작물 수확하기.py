T = int(input())

for tc in range(1,1+T):
    N = int(input()) # 농장의 크기
    farm = [list(map(int,input())) for _ in range(N)]
    #
    # print(farm)
    # 수확 값
    show_money = 0

    # 수확한 수익 출력하기
    for i in range(N):
        # 양쪽 값 더해주기
        if 0<= i < (N // 2): # 중간 지점 전까지 계산, 가운데 열 값 제외
            show_money += farm[i][N // 2]  # 가운데 열 값 더해주기
            for a in range(1,i+1): # 중간에서 a만큼 떨어진 값들 반복해서 전체 값에 더해주기
                before_duo = farm[i][N//2-a] + farm[i][N//2+a]
                show_money += before_duo
        #
        if (N // 2) < i < N: # 중간 지점 후부터 계산, 가운데 열 값 제외
            show_money += farm[i][N // 2]  # 가운데 열 값 더해주기
            for a in range(N-i-1,0,-1): # 인덱스가 줄어드는데 (전체 길이-현재 i값)부터 1씩 줄어들며 더해줌
                after_duo = farm[i][N//2-a] + farm[i][N//2+a]
                show_money += after_duo

        if i == (N//2): # 중간 지점 계산
            for j in range(N):
                show_money += farm[i][j]



    print(f"#{tc} {show_money}")
