from collections import deque
def solution(s):
    answer = True
    remained_lst = deque()
    for idx in range(len(s)):
        if s[idx] == ')':
            if remained_lst:
                answer = True
                remained_lst.pop()
            else:
                answer = False
                break
                
        elif s[idx] == '(':
            remained_lst.append('(')
    
    if remained_lst:
        answer = False
            
    return answer 