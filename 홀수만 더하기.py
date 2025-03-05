T = int(input())

for tc in range(1,1+T):
    num_lst = list(map(int,input().split())) # 인풋 리스트로 받기

    sum_num = 0 # 홀수들 더해줄 변수
    for i in range(len(num_lst)): # 리스트의 길이만큼 반복해서 홀수면 더해주기
        if num_lst[i] % 2 == 1: # 나눴을때 나머지가 1일때 홀수니까
            sum_num += num_lst[i] # 변수에 더해주기 

    print(f"#{tc} {sum_num}") # 출력해주기