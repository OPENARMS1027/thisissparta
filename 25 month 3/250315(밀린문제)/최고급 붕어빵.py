T = int(input())

for tc in range(1,1+T):
    # N명의 사람들이 자격을 얻어서
    # M초마다 K개의 붕어빵 뽑아냄
    N,M,K = map(int,input().split())
    # N명 사람들의 도착 시간
    time = list(map(int,input().split()))    
    time.sort() # 도착 시간별 정렬
    answer = 'Possible'

    for i in range(N):
        if time[i] < M: # 나오는 시간보다 일찍오면 그냥 불가능
            answer ='Impossible'
        '''
        손님이 도착했을 시간에 나왔어야 할 빵 개수보다
        앞 사람들이 가져간 빵의 개수(현재 차례 사람의 idx)가 더 많다면
        빵을 나눠줄 수 없음 
        ''' 
        
        if (time[i]//M * K) - (i) <= 0:
            answer = 'Impossible'
    
         

    print(f"#{tc} {answer}")
    
    