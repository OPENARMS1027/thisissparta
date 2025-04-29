
my_bingo = [list(map(int,input().split())) for _ in range(5)]
call_bingo = [list(map(int,input().split())) for _ in range(5)]

# 시작
for i in range(5):
    for j in range(5):
        # 빙고판 확인하기
        count = 0 # 빙고 카운트
        for a in range(5):
            for b in range(5):
                if call_bingo[i][j] == my_bingo[i][j]:
                    my_bingo[i][j] = 0

                
                if i >= 2 and j >= 2:



