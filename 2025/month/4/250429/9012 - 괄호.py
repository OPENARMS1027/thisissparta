# 순서가 맞지않으면 VPS가 아니다.

def find_vps(candidate):
    answer = 'YES'
    stack = []
    length = len(candidate)
    for i in range(length):
        if candidate[i] == '(':
            stack.append(candidate[i])

        elif candidate[i] == ')':
            if stack:
                stack.pop()
            else:
                answer = 'NO'
                return answer
    else:
        if stack:
            answer ='NO'
            return answer
        
    return answer
        
T =int(input())
for _ in range(T):
    vps_candidate = input()
    result = find_vps(vps_candidate)
    print(result)