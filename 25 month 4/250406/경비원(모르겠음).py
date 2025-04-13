x,y = map(int,input().split()) # 블록 가로 세로
N = int(input()) # 상점 개수
stores = []
# 상점 위치
for _ in range(N):
    a,b = map(int,input().split())
    stores.append((a,b))

position, delta = map(int,input().split()) # 동근이 위치
total_distance = 0

