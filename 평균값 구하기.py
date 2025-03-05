T = int(input())

for tc in range(1,1+T):
    num_lst = list(map(int,input().split()))
    sum_ans = 0 # 리스트 값 다 더해줄 변수
    # 다 더해서 길이만큼 나눠주면 평균값

    for i in range(len(num_lst)): # 리스트의 길이만큼 반복해서 더해주기
        sum_ans += num_lst[i] # 계속 값 더해주기
    answer = float(sum_ans / len(num_lst)) # 개수만큼 나눠서 평균값 구하기
    answer = round(answer) # round : 반올림 해주는 함수 # round(number,자릿수)
    print(f"#{tc} {answer}")