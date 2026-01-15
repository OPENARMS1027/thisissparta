def solution(numbers, target):
    answer = 0 
    
    def dfs(idx,cur):
        nonlocal answer 
        if idx == len(numbers):
            if cur == target:
                answer += 1
            return
        
        dfs(idx + 1, cur + numbers[idx])
        dfs(idx + 1, cur - numbers[idx])
    
    dfs(0,0)
    return answer

"""
nonlocal 주의
bfs에서 종료 조건을 줄 때 조건을 잘 확인하기 

"""