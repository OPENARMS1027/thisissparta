N = int(input())
paper = [[False] * 100 for _ in range(100)]
# 색종이가 덮은 부분을 True로 덮지 않은 부분은 False로 설정
extent = 0 # 넓이
for k in range(N):
    x, y = map(int,input().split())
    # 리스트 돌면서 10칸씩 색칠해주기
    for i in range(10):
        for j in range(10):
            if paper[x + i][y +j] == False:
                paper[x + i][y +j] = True

for i in range(100):
    for j in range(100):
        if paper[i][j]:
            extent +=1

print(extent)
