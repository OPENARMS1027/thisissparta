N = int(input()) # 스위치 개수
switch = list(map(int,input().split()))
M = int(input()) # 학생 수
for i in range(M):
    sex, num = map(int,input().split())

    # 남자일 때 1
    if sex == 1:
        # i*num -1 이 실제 인덱스
        for i in range(1,N // num +1):
            if i*num - 1 >=N:
                break

            if switch[i*num-1] == 1:
                switch[i * num - 1] = 0
            else:
                switch[i * num - 1] = 1

    # 여자일 때 1
    else:
        if switch[num-1] == 1:
            switch[num-1] = 0
        else:
            switch[num-1] = 1
        idx = num - 1
        for i in range(1,N//2):
            # 범위내에 있을 때
            if idx-i < 0 or idx+i >=N:
                break
                # 기준점 양쪽이 같다면
            if switch[idx-i] == switch[idx+i]:
                if switch[idx-i] == 1:
                    switch[idx-i] = 0
                    switch[idx+i] = 0
                else:
                    switch[idx-i] = 1
                    switch[idx+i] = 1
            else:
                break

for i in range(1,N+1):
    print(switch[i-1], end=' ')
    if i % 20 == 0:
        print()