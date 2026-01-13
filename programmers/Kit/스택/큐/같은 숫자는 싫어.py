from collections import deque
def solution(arr):
    answer = deque()
    
    answer.append(arr[0])
    for num in arr:
        if answer[-1] != num:
            answer.append(num)
    answer = list(answer)
    return answer


"""
JSON = 데이터 교환 규격, 문자열 포맷(규칙)
JSON 표준 타입은 객체,배열, 문자,넘버,불리언,null만 가능
이 6개 말고는 JSON에 없기 때문에
deque은 JSON으로 표현 가능한 규격으로 바꿔줘야 한다. 

즉 파이썬 내부에서 사용한 후, 밖으로 내보내는 순간(JSON 응답)에는
바꿔줘야 한다. 
"""