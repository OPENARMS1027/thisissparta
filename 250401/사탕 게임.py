

def count():
    global max_count
    for i in range(N):
        # count_r : 행을 확인, count_c : 열을 확인
        count_c = count_r = 1
        for j in range(1,N):
            if candies[i][j-1] == candies[i][j]:
                count_r +=1
                
            else:
                max_count = max(count_r,max_count)
                count_r = 1
                

            if candies[j-1][i] == candies[j][i]:
                count_c += 1
               
            else:  
                max_count = max(count_c,max_count)
                count_c = 1

        # 끝까지 다 같을 때 대비
        max_count = max(count_r,max_count)
        max_count = max(count_c,max_count)

        
        
        


N = int(input())
candies = [list(map(str,input())) for _ in range(N)]

max_count = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N and candies[i][j] != candies[i][j+1]:
            candies[i][j+1],candies[i][j] = candies[i][j], candies[i][j+1]
            count()
            candies[i][j+1],candies[i][j] = candies[i][j], candies[i][j+1]
        
   
        if j + 1 < N and candies[j][i] != candies[j+1][i]:
            candies[j+1][i],candies[j][i] = candies[j][i], candies[j+1][i]
            count()
            candies[j+1][i],candies[j][i] = candies[j][i], candies[j+1][i]
print(max_count)