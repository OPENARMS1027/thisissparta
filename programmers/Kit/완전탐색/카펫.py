def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for h in range(1,int(total**0.5)+1):
        if total % h != 0:
            continue
        
        w = total / h
        print(w)
        if (w-2) * (h-2) == yellow:
            answer.append(w)
            answer.append(h)
    
    return answer

"""
방정식으로 만들어지는 식을 어떻게 완탐으로 할지 ?
제곱근을 이용한 약수 찾기! 주의
int로 유리수를 바꿔주는 작업 주의
"""