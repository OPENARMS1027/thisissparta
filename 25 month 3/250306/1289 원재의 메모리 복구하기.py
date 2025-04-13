T =int(input())

for tc in range(1,1+T):
    memory = list(map(int,input())) # 원래 상태
    now = [0] * len(memory) # 현재 상태 리스트 # 계속 바꿔줄 리스트
    # 모든 bit가 0인 초기 상태에서 원래대로 돌아가는데 걸리는 횟수
    counts = 0 # 횟수 세줄 변수

    for i in range(len(now)): # 리스트 길이만큼 반복
        if memory[i] != now[i]: # 만약 같은 인덱스의 리스트 요소가 다르다면
            for a in range(i,len(now)): # 시작점부터 끝까지 반복 돌리기
                if memory[i] == 1: # 다를때 1이라면 ? 현재리스트도 1로 바꿔주기
                    now[a] = 1

                elif memory[i] == 0: # 다를때 1이라면 ? 현재리스트도 0로 바꿔주기
                    now[a] = 0
            counts += 1 # 리스트에서 하나의 요소 확인하고 바꿀때마다 횟수 세주기


    print(f"#{tc} {counts}")

