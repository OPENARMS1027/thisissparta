T = int(input())

for tc in range(1,1+T):
    N, K = map(int,input().split()) # 학생 수 N, 학생의 번호 K

    scores = []
    K = K-1 # 리스트 안에서 인덱스 관리 때문에 -1


    for i in range(N): # N개의 리스트 다른 줄에 받기
        score_lst = list(map(int,input().split())) # 점수 리스트로 받기
        score = 0.35 * score_lst[0] + 0.45 * score_lst[1] + 0.2 * score_lst[2] # 점수계산
        scores.append(score) # 점수 리스트에 넣기

        if i == K: # 주어진 번호의 학생이면
            k_student = score # 점수 따로 저장해주기

    scores.sort() # 점수 리스트 오름차순 정리하기


    idx = scores.index(k_student) # 정렬된 리스트에서 특정 번호 학생의 인덱스
    #
    # print(idx)
    #
    #

    grade = ['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+'] # 학점 리스트
    answer = 0
    # 인덱스가 어느 학점의 범위 안인지 확인하기
    for i in range(0,N,N/10): # 인덱스는 정수만 되니까 몫으로 다뤄줘야 함.
        if i <= idx < i+(N/10): # 범위 안에 특정 학생의 인덱스가 있으면
            answer = grade[i//(N/10)]

    print(f"#{tc} {answer}")