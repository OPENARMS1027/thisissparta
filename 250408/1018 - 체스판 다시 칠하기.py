'''
체스판 형태에 맞춰서 다시 색칠해주는데
최소한으로 색칠해 줄 때의 개수
정상적인 체스판으로 고쳐주기
r,c 의 합을 2로 나눈 나머지 값에 따라 정해지는 색깔
'''

N,M = map(int,input().split())
chess = [list(map(str,input())) for _ in range(N)]
min_count = float('inf')

for r in range(N-8+1):
    for c in range(M-8+1):
        w_count = 0
        b_count = 0
        for i in range(8):
            for j in range(8):
                cur = chess[r+i][c+j]
                # 정상적인 체스판의 종류는 두 종류
                # 두 가지를 모두 판단해서 적은 걸로
                if (i+j) % 2 == 0:
                    if cur != 'W':
                        w_count += 1
                    if cur != 'B':
                        b_count += 1
                else:
                    if cur != 'B':
                        w_count += 1
                    if cur != 'W':
                        b_count += 1

        min_count = min(min_count,b_count,w_count)

print(min_count)