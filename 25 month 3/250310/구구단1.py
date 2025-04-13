T = int(input())

for tc in range(1,1+T):
    N = int(input()) # N이 1이상 9이하의 두 수 a,b의 곱으로 표현될 수 있는지

    num_lst = [1,2,3,4,5,6,7,8,9] # 숫자 확인할 리스트
    answer = 'No' # 기본으로 안된다고 가정
    count = 0 # 2회 되는지 세어줄 변수
    for i in range(9,0,-1): # 1부터 시작하면 1이 항상 들어가기 때문에 큰 값부터 나눠주기
        if N % i == 0: # N이 i로 나누었을 때 나머지가 0ㅇ라면
            N = N // i # N값 재할당
            count += 1 # count 추가해주기
            if N in num_lst and count == 1: # 재할당된 N이 num_lst에 있고 count 가 1이라면
                # 결국 2개로 표현이 되기 때문에 합당한 조건
                answer = 'Yes' # answer를 yes로 변경
        if count > 2: # count가 2가 넘어간다면 그대로 종료 (no인채로)
            break

    print(f"#{tc} {answer}")

