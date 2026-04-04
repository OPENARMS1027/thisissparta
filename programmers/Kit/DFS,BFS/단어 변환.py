from collections import deque         
        
def solution(begin, target, words):
    
    def bfs(now_word,goal,words):
        nonlocal answer
        now = deque()
        visited = [False] * len(words)
        now.append((now_word,0))

        while now:
            cur, dist = now.popleft()

            if cur == goal:
                answer = dist
                return 

            for a in range(len(words)):
                if not visited[a]: 
                    count = 0
                    for idx in range(len(cur)):
                        if cur[idx] == words[a][idx]:
                            count += 1

                    if count == (len(cur) - 1):
                        now.append((words[a],dist+1))
                        answer += 1
                        visited[a] = True   

    answer = 0
    
    if target not in words:
        return answer
    
    else:
        bfs(begin,target,words)
        
    
    return answer