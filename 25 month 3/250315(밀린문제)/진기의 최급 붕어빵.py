import sys
sys.stdin = open("input.txt","r")

T = int(input())

for tc in range(1,1+T):

    # if tc != 2:
    #     continue
    # N명의 사람, M초의 시간마다 K개 붕어빵
    N,M,K = map(int,input().split())
    # N명의 사람이 언제 도착하는지 시간 리스트
    arrived_time = list(map(int,input().split()))
    arrived_time.sort() # 도착순서대로 정렬
    bread_lst = [0] * (11112) # 빵개수 확인 리스트

    answer = 'Possible' # 가능하다고 전제

    # for i in range(M+M,11112,M):
    #     bread_lst[i] = bread_lst[i-M] + K
    #     for k in range(1,N):
    #         if i+k < 11112:
    #             bread_lst[i+k] = bread_lst[i]
    
    # 빵 개수랑 사람 도착 시간 비교해서 빵 있는지 없는지 확인
    for i in range(N):
        if bread_lst[arrived_time[i]] < 1: 
            answer = 'Impossible'
            break
        else: # 만약 빵이 있는 상태라면
            # 만들 수 있는 빵 개수 리스트에서 하나씩 빼줘서
            # 다음 손님 빵 줄 수 있는지 확인할 리스트 최신화
            for k in range(arrived_time[i]+1,11112):    
                bread_lst[k] -= 1    
        
    print(f"#{tc} {answer}")