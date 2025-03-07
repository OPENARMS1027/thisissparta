T = int(input())

for tc in range(1,1+T):
    puzzle = [list(map(int,input().split())) for _ in range(9)] # 퍼즐이 9x9 고정

    # 흠 없는 스도쿠 퍼즐이라고 가정
    answer = 1

    # 행 검사
    for i in range(9):
        sum_set_i = set()
        for j in range(9):
            sum_set_i.add(puzzle[i][j]) # 퍼즐의 값을 만들어준 set에 넣어주기
        if len(sum_set_i) != 9:
            answer = 0
            break

    # 열 검사
    for i in range(9):
        sum_set_j = set()
        for j in range(9):
            sum_set_j.add(puzzle[j][i]) # 퍼즐의 값을 만들어준 set에 넣어주기
        if len(sum_set_j) != 9:
            answer = 0
            break

    # 9칸 검사
    for i in range(0,6,3): # 행 3칸씩 나눠서 반복 돌려주기
        for j in range(0,6,3): # 열 3칸씩 나눠서 반복 돌려주기
            nine_check = set()
            for k in range(3): # 3칸씩 나눈 j를 순회하기
                for a in range(3): # 3칸씩 나눈 i를 순회하기
                    nine_check.add(puzzle[i+k][j+a])
            if len(nine_check) != 9:
                answer = 0
                break

    print(f"#{tc} {answer}")

