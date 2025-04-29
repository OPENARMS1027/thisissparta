'''
조건대로 인접한 두개가 다르다면 바꿔주고 배열 돌면서 최대값 갱신해주기
'''
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

# 이차원 배열 돌면서 다를때마다 바꿔주고 확인해보기 
for i in range(N):
    for j in range(N):
        # 행마다 체크
        # 범위 내고 인접한 두개가 다르다면 
        if j + 1 < N and candies[i][j] != candies[i][j+1]:
            candies[i][j+1],candies[i][j] = candies[i][j], candies[i][j+1] #바꿔주고
            count() # 세보고 최대값 최신화
            candies[i][j+1],candies[i][j] = candies[i][j], candies[i][j+1] # 다시 바꿔주기
        
        # 열마다 체크
        if j + 1 < N and candies[j][i] != candies[j+1][i]:
            candies[j+1][i],candies[j][i] = candies[j][i], candies[j+1][i]
            count()
            candies[j+1][i],candies[j][i] = candies[j][i], candies[j+1][i]
print(max_count)