T = int(input())

for tc in range(1,1+T):
    N,M = map(int,input().split()) # 길이 입력값 받기
    a = list(map(int,input().split())) # a 배열
    b = list(map(int,input().split())) # b 배열
    
    max_sum = 0 # 최대값 초기화

    sum_ab_list = [] # 합 넣어줄 빈 리스트
    if N < M: # b가 더 길 때
        for i in range(M-N+1): # 작은 리스트의 길이 만큼 긴 리스트의 처음 인덱스를 제한해서 범위를 맞춰줌
            sum_ab = 0  # 합 초기화ㅣ
            for k in range(N): # 작은 리스트의 정해진 길이만큼 반복
                sum_ab += a[k] * b[i+k] # a는 정해진 길이만큼 반복, b는 같은 길이지만 1씩 늘어나는 인덱스
            if max_sum < sum_ab: # 한 번 돌때 값이 이전값보다 크다면 
                max_sum = sum_ab  # 재할당 해주기

    
    elif N > M: # a가 더 길때
        for i in range(N-M+1):
            sum_ab = 0  
            for k in range(M):
                sum_ab += b[k] * a[i+k]
            if max_sum < sum_ab:
                max_sum = sum_ab 

    print(f"#{tc} {max_sum}")
