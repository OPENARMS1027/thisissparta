# 조건 만족하는 예비 후보지 개수 출력

T = int(input())
for tc in range(1,1+T):
    N,M = map(int,input().split()) # N x M의 구역 정보

    candidates = 0
    # 구역 정보 2차원 리스트로 input
    landing_spots = [list(map(int,input().split())) for _ in range(N)] # 2차원 리스트로 정보 받기

    # 행과 열 반복하며 2차원 리스트 순회
    for r in range(N): 
        for c in range(M): 
            low_terrains = 0 # 낮은 지형 있는지 확인하고 할당해줄 변수
            # 주변 8개의 지형 확인 할 델타
            for dr, dc in ([0,1],[1,0],[0,-1],[-1,0],[-1,1],[1,1],[1,-1],[-1,-1]):
                nr = r + dr # 주변 8개 지형의 r값
                nc = c + dc # 주변 8개 지형의 c값
                # 만약 범위 안이고 예비 후보지의 높이가 주변 8개의 각 지형보다 높다면 세주기
                if 0<=nr<N and 0<=nc<M and landing_spots[nr][nc] < landing_spots[r][c]:
                    low_terrains += 1
            
            # 각 후보지마다 체크한 낮은 지형이 4개 이상이라면 후보지로 선정
            if low_terrains >= 4:
                candidates += 1   

    print(f"#{tc} {candidates}")            




