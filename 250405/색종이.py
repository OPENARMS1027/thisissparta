N = int(input())
paper = [[False] * 100 for _ in range(100)]
# 색종이가 덮은 부분을 True로 덮지 않은 부분은 False로 설정
extent = 0 # 넓이
for k in range(N):
    extent += 100
    x, y = map(int,input().split())
    # 리스트 돌면서 10칸씩 색칠해주기
    for i in range(10):
        for j in range(10):
            # 색이 이미 칠해졌다면 겹치는 부분이니까 9로 표시해주기
            if paper[x + i][y +j] == True:
                paper[x + i][y +j] = 9

            # 색이 칠되지 않았으면 칠해주기
            elif paper[x + i][y +j] == False:
                paper[x + i][y +j] = True

for i in range(100):
    for j in range(100):
        if paper[i][j] == 9:
            extent -= 1

print(extent)


