def to_sec(t):
    mm, ss = map(int,t.split(':'))
    return mm*60 + ss

def to_time(t):
    mm = t // 60
    ss = t % 60
    result = f'{mm:02d}:{ss:02d}'
    return result
    

def solution(video_len, pos, op_start, op_end, commands):
    total_len = to_sec(video_len)
    cur = to_sec(pos)
    start = to_sec(op_start)
    end = to_sec(op_end)
    
    for com in commands:
        if start <= cur <= end:
                    cur = end 
            
        if com == 'prev':
            if cur <= 10:
                cur = 0
                continue
            cur -= 10
            
        elif com == 'next':
            if total_len - cur <= 10:
                cur = total_len
                continue
            cur += 10
            
        if start <= cur <= end:
            cur = end 
        
    answer = to_time(cur)
    return answer