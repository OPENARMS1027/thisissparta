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
        show_money += farm[i][N // 2] # 중간 값 더해주기
        # 양쪽 값 더해주기
        for k in range(i+1):
            if 0 < k <= N//2:
                money = farm[i][(N//2)-k] + farm[i][(N//2)+k]
                show_money += money

        if i > (N // 2):  # 가장 긴 중간 지점을 넘어 갔을 때
            for a in range(N-i):
                if 0 < a:
                    money = farm[i][N-k] + farm[i][N-k]
                    show_money += money

    print(f"#{tc} {show_money}")
