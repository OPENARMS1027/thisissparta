T = int(input())

for tc in range(1,1+T):
    # 문제 좀 제대로 읽기
    # 횟수를 세는 것이 아닌 0부터 9까지의 숫자가 다 나왔을때의 양의 번호
    # 양의 번호를 읽어주는 것임
    N =int(input()) # N의 배수 번호로 양 세기
    num_set = set() # 빈 set 만들어주기

    value_N = N # 고정된 N의 값 변수


    while len(num_set) != 10:
        for i in range(len(str(N))): # 문자 길이만큼 반복
            num_set.add(str(N)[i]) # 각 문자 set에 추가
            # 횟수 세어주기

        if len(num_set) == 10: # set의 개수가 10이면 break
            break
        N = N + value_N  # N 재할당

    print(f"#{tc} {N}")
             