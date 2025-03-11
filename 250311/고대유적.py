# 가장 긴 구조물의 길이 찾기
# 서로 평행 또는 직각으로만 자리하고 있음
# 구조물 있는 곳 1, 없는 곳 0
#

T = int(input())

for tc in range(1,1+T):
    N,M = map(int,input().split()) # N x M의 사진 해상도

    # 구조물이 있는지 없는지 데이터 2차원 배열로 받기
    picture = [list(map(int,input().split())) for _ in range(N)]
    max_len_structure = 0

    # 행과 열을 탐색하머 가장 긴 구조물 찾기
    # 직선 형태이기 때문에 행별 탐색, 열별 탐색을 진행해준다.
    # 1일 때 구조물이 시작, 쭉 세다가 0이 나오면 길이 변수 추가 멈춰주기

    # 행별 탐색
    for r in range(N):
        start = False # 구조물 탐색 알림
        len_structure = 0
        for c in range(M):
            if picture[r][c] == 1: # 구조물 있다면
                len_structure += 1 # 길이에 추가
                start = True # 구조물이 시작됐음을 갱신
                # 사진 끝자락까지 구조물이 있을 때 최대값 비교 후 해당하면 갱신
                if c == M-1: # 구조물 탐색하던 중 사진 끝자락이면
                    if max_len_structure < len_structure:
                        max_len_structure = len_structure 
            # 구조물이 계속 없었다면 배제
            elif picture[r][c] == 0 and start: # 구조물이 없다면 start 갱신 해주고
                start = False # 구조물이 끝났음을 갱신
                
                # 구조물 하나의 길이 세기가 끝났을 때 최대값이랑 비교
                if max_len_structure < len_structure:
                    max_len_structure = len_structure
                len_structure = 0    

    # 열별 탐색
    for c in range(M):
        start = False # 구조물 탐색 알림
        len_structure = 0
        for r in range(N):
            if picture[r][c] == 1:  # 구조물 있다면    
                len_structure += 1  # 길이에 추가
                start = True # 구조물이 시작됐음을 갱신
                # 사진 끝자락까지 구조물이 있을 때 최대값 비교 후 해당하면 갱신
                if r == N-1: # 구조물 탐색하던 중 사진 끝자락이면
                    if max_len_structure < len_structure:
                        max_len_structure = len_structure 
            # 구조물이 계속 없었다면 배제
            elif picture[r][c] == 0 and start: # 구조물이 없다면 start 갱신 해주고
                start = False # 구조물이 끝났음을 갱신

                # 구조물 하나의 길이 세기가 끝났을 때 최대값이랑 비교
                if max_len_structure < len_structure:
                    max_len_structure = len_structure
                len_structure = 0    

    print(f"#{tc} {max_len_structure}")



