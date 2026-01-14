from collections import deque
def solution(priorities, location):
    q = deque([(p,i) for i,p in enumerate(priorities)])
    answer = 0
    
    while q:
        pri, idx = q.popleft()
        
        if any(pri <p for p,_ in q):
            q.append((pri,idx))
        else:
            answer += 1
            if idx == location:
                return answer
