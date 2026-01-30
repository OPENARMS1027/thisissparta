def solution(k, dungeons):
    
    answer = -1
    dungeons.sort(key=lambda x: x[0], reverse=True)
    visited = [False] * len(dungeons)
    
    def dfs(cur,cnt):
        nonlocal answer
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= cur:
                visited[i] = True
                dfs(cur - dungeons[i][1], cnt + 1)
                visited[i] = False
    dfs(k,0)
            
        
    return answer
