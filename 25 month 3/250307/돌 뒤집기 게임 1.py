T  = int(input())

for tc in range(1,1+T):
    N,M = map(int,input().split()) # N개 돌, M번만큼 바꿔주기
    arr = list(map(int,input().split())) # 초기 돌의 상태

    for _ in range(M):
        i,j = map(int,input().split()) # i번 돌부터 j개만큼 색 바꿔주기(i번 돌부터)

        # i번째지만 인덱스로는 -1 해줘야 함
        i = i -1
        # i번째부터 j개 돌아서 바꾸기
        for a in range(i,i+j):
            if a < N: # a의 범위가 초과하지 않을 때
                if arr[i] == 0: # i번 돌 색으로 맞춰줘야해서
                    arr[a] = 0 # 반복을 돌며 j개의 돌을 색을 맞춰준다
                elif arr[i] == 1: # 다른 돌 색이라면
                    arr[a] = 1 # 그 돌 색으로 맞춰주기

    print(f"#{tc}",*arr)
