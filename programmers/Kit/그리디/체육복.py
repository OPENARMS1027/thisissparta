def solution(n, lost, reserve):
    answer = 0
    students = [1] * n
    
    for stu in lost:
        students[stu-1] -= 1
    
    for stu in reserve:
        students[stu-1] += 1 
        
    for idx in range(n):
        if students[idx] == 0:
            if idx -1 >= 0 and students[idx-1] >= 2:
                students[idx-1] -= 1
                students[idx] += 1
            elif idx +1 < n and students[idx+1] >= 2:
                students[idx+1] -= 1
                students[idx] += 1 
    
    for stu in students:
        if stu:
            answer += 1
    
    
    return answer

