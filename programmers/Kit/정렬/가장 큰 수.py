def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    answer += str(int(''.join(numbers)))
    
    return answer


"""
주의!
lambda의 의미, 타입 변환, numbers의 원소에 0이 들어감
"""