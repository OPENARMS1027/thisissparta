T = int(input())

for tc in range(1,1+T):
    # 지도 한 변의 크기인 N, 경사로길이인 N
    N,T = map(int,input().split()) 
    field = [list(map(int,input().split())) for _ in range(N)]

    
    # 행별 순회
    for i in range(N):
        stack= []
        top = -1
        count = 0
        for j in range(N):
            if stack and stack[top] != field[i][j]:  
                
            
            top += 1
            stack.append(field[i][j])
            
            

            
        
                
    # 열별 순회