# 교착은 아래위로만 판단
# 남아있는 테이블 교착상태 반환
# 1은 N극 2는 S극

for tc in range(1,11):
    N = int(input()) # 항상 100, 정사각형 테이블의 한 변의 길이
    arr = [list(map(int,input().split())) for _ in range(100)] # 테이블의 초기 모습

    counts = 0 # 교착 상태 세어 줄 변수
    # 항상 변의 길이가 100인 정사각형 테이블에서
    for j in range(100):
        s_j = 0 # s인 j값
        n_j = 0 # n인 j값
        queue_s = []
        queue_n = []

        for i in range(100):
            # 세로의 형태만 고려해준다.
            if arr[i][j] == 2:
                s_j = j
                queue_n.append(s_j)
            elif arr[i][j] == 1:
                n_j = j
                queue_s.append(n_j)

        # 두 개의 큐중 더 짧은 것 길이 기준으로 비교
        if len(queue_s) > len(queue_n):
            for i in range(len(queue_n)):
                if queue_s[0] > queue_n[0]:
                    counts += 1
        else:
            for i in range(len(queue_s)):
                if queue_s.pop(0) > queue_n.pop(0):
                    counts += 1



    print(f"#{tc} {counts}")
