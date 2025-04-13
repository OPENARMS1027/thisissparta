T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split()) # 돌의 수 N, 뒤집기 횟수 M
    arr = list(map(int,input().split()))

    # 뒤집기 횟수만큼 입력을 받고 받을 때마다 실행해 줌. 따라서 반복문 안에서 입력과 실행 모두 이루어 짐


    for _ in range(M):
        i,j = map(int,input().split()) # i번째 돌을 사이에 두고 마주보는 j개의 돌
        # 1번 문제와 같이 i번째 돌이기 때문에 리스트에서 사용시 인덱스 수정 필요
        i = i - 1

        for a in range(1,j+1): # j의 개수만큼 반복
            if 0<=i-a and i+a <N: # i를 중심으로 양쪽에 있는 원소들의 인덱스가 리스트 내일 때
                if arr[i-a] == arr[i+a]: # 만약 마주보는 원소가 같고
                    if arr[i-a] == 1: # 그게 1로 같을 때 뒤집기
                        arr[i+a] = 0
                        arr[i-a] = 0
                    else: # 0으로 같을 때 뒤집기
                        arr[i+a] = 1
                        arr[i-a] = 1

    print(f"#{tc}", *arr)





