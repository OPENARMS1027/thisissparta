from collections import deque
def solution(n, computers):
    count = 0 
    visited = [False] * n
    
    def dfs(index):
        nonlocal visited, count
        q = deque()
        q.append(idx)
        visited[idx] = True
        
        while q:
            cur = q.popleft()
            cur_r = computers[cur]
            for index in range(len(cur_r)):
                if index != cur and cur_r[index] and not visited[index]:
                    q.append(index)
                    visited[index] = True

    for idx in range(n):
        if visited[idx]:
            continue
        dfs(idx)
        count += 1 
        
    

    return count 


"""
2차원 배열에서 idx랑 값이랑 헷갈리기 없음!!!
반복문 돌릴 때 착각하면 아주 큰 오류가 발생
"""