T = int(input())
for tc in range(1,1+T):
    N, Q = map(int,input().split()) # N개의 상자, Q회 동안 변경
    boxes = [0] * (N) # 인덱싱 편하게 해줄려고 +1개 해줌

    for i in range(1,Q+1):
        # i번째 작업에 대해  # L번 상자부터 R번 상자까지 값 i로 변경
        L, R = map(int,input().split()) 
    #     # 1번부터니까 idx 조정해주기
        L = L- 1 #박스의 idx
        R = R -1 #박스의 idx

        for a in range(L,R+1): # L부터 R박스까지 i로 값 변경해주기
            boxes[a] = i
    
    print(f"#{tc}",*boxes)  
    
        

        
        



        