def solution(array, commands):
    answer = []
    
    for command in commands:
        first,end,idx = command
        new_array = array[first-1:end]
        new_array.sort()
        answer.append(new_array[idx-1])
            
    return answer