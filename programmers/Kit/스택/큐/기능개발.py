from collections import deque
def solution(progresses, speeds):
    answer = []
    remained = [0] * len(progresses)
    for idx in range(len(speeds)):
        work_day = 100 % speeds[idx]
        if work_day != 0:
            remained[idx] = (100-progresses[idx])// speeds[idx] + 1
        else:
            remained[idx] = (100-progresses[idx] )// speeds[idx]
    
    # print(remained)
    
    answer.append(1)
    max_count = remained[0]
    for idx in range(1,len(remained)):
        if max_count < remained[idx]:
            answer.append(1)
            max_count = remained[idx]
        else:
            answer[-1] += 1
    
    # print(answer)
    """
    완료까지 걸리는 날짜를 계산한 배열을 통해서 
    묶음(최대)를 비교해가며 카운트
    """
    return answer