def solution(sizes):
    answer = 0
    max_val = 0
    min_val = 0 
    
    for w,h in sizes:
        big = max(w,h)
        max_val = max(max_val,big)
        small = min(w,h)
        min_val = max(min_val,small)
        
    answer = max_val * min_val
        
    return answer


"""
max * max 지만 min 중에 max인거 참고
시간복잡도 정리 참고
"""