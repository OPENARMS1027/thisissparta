N = int(input())
line = list(map(int,input().split()))

list = [] # 줄
for i in range(N):
    # insert 메서드 이용
    # 현재 전체 길이에서 재낄만큼 앞으로 땡긴 index
    list.insert((i+1)-(line[i]+1),i+1)

print(*list)


