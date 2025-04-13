N, M = map(int,input().split())
board = [list(map(str,input())) for _ in range(N)]

# 지민이가 다시 칠해야 하는 정사각형의 최소 개수 구하기
min_count = float('inf')

for i in range(N-8+1):
    for j in range(M-8+1):
        count = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if board[i][j] == 'W':
                    if b % 2 == 0 and board[a][b] != 'W':
                        count += 1
                    elif b % 2 == 1 and board[a][b] != 'B':
                        count += 1

                        
                else:
                    if b % 2 == 0 and board[a][b] != 'B':
                        count += 1
                    elif b % 2 == 1 and board[a][b] != 'W':
                        count += 1

        min_count = min(min_count,count)

print(min_count)            
                
