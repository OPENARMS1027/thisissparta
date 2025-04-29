# 교착은 아래위로만 판단
# 남아있는 테이블 교착상태 반환
# 1은 N극 2는 S극
# 위가 N극이고 밑이 S극이기 때문에 N 자성체가 먼저 위에 나오고 S 자성체가 아래 나오면 교착이 생성된다.
# 따라서 짝을 이루기 때문에 True, False를 이용해서 자성체가 나오는 것을 확인해 줌
# N 자성체가 나오면 False로 먼저 설정, 그리고 S 자성체가 나오면 True로 변경 후 카운트
#

for tc in range(1,11):
    N = int(input()) # 항상 100, 정사각형 테이블의 한 변의 길이
    arr = [list(map(int,input().split())) for _ in range(100)] # 테이블의 초기 모습

    counts = 0 # 교착 상태 세어 줄 변수
    # 항상 변의 길이가 100인 정사각형 테이블에서
    for c in range(100):

        check_n = False # 자성체가 쌍을 이뤄 교착하는 것을 확인하기 위함
        for r in range(100): # 세로로만 봐주기 때문에 열은 그대로고 행을 변화시키며 탐색
            if arr[r][c] == 1: # N을 만나면
                check_n = True # 체크
            elif arr[r][c] == 2: # S를 만나면
                if check_n: # N이 앞에 있었다면
                    counts += 1 # 카운트 해준 뒤
                    check_n = False # 다시 짝을 맞추기 위해 초기화 해준다.

    print(f"#{tc} {counts}")
