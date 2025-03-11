T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split()) # M개씩 N개의 줄에 있는 풍선

    balloons = [list(map(int,input().split())) for _ in range(N)]

    # 풍선 선택시 날릴 수 있는 꽃가루의 합 중 최대값을 출력하는 프로그램 만드시오

    # 최대값 변수 설정
    max_balloons = 0
    # 행, 열 순회
    for r in range(N):
        for c in range(M):
            each_sum_balloons = 0 # 각 좌표를 순회할때마다 더해줄 변수, 그리고 그 변수를 돌 때마다 초기화
            each_sum_balloons += balloons[r][c] # 순회할 중심 좌표
            for k in range(1,balloons[r][c]+1): # 1부터 시작해줘야 해당 중심좌표 값만큼 순회
                for dr, dc in([0,1],[1,0],[0,-1],[-1,0]): # 델타 탐색
                    nr = r + k*dr # 움직일 좌표 설정
                    nc = c + k*dc # 움직일 좌표 설정
                    if 0<= nr < N and 0<= nc <M: # 범위 내에 있다면
                        each_sum_balloons += balloons[nr][nc] # 각 좌표 순회마다 변수에 더해줌

            # 최대값 갱신
            if max_balloons < each_sum_balloons: # 좌표의 sum 값이 더 크다면
                max_balloons = each_sum_balloons # 최대값 갱신

    print(f"#{tc} {max_balloons}")

