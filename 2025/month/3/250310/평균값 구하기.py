T = int(input())

for tc in range(1,1+T):
    num_lst = list(map(int,input().split())) # 리스트형태로 입력받기

    sum_num = 0 # 더한값 넣어줄 변수

    for i in range(len(num_lst)): #리스트의 길이만큼 반복해주며 값 더해주기
        sum_num += num_lst[i] # 받은 값들을 하나하나 더해주기
    
    answer = sum_num / len(num_lst) # 길이만큼 나눠서 평균값 구해주기


    print(f"#{tc} {round(answer)}") # round함수 이용해서 반올림해주기
    # round의 경우 반점 후 뒤에 숫자를 써주면
    # 해당 자리의 숫자 만큼 소수점을 표현해준다 ( 그 아래 소수점에서 반올림해서)