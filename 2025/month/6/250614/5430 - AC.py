# 문장열로 받았을 때 deque으로 바꾸려면 리스트로 파싱해야 함
# return 은 아무것도 명시하지 않으면 기본값이 "None" - 함수의 리턴값을 생각 ! 
# 결과값이 빈 배열인 경우 반례 생각
# join은 리스트를 다루는데 리스트 안의 "문자열 요소"들을(숫자 안됨) 하나의 문자열로 이어붙이는 작업 -- > 결과물은 항상 "하나의 문자열"


def cal():
    global nums_lst
    reverse_state = False
    for a in range(len(p)):
        if p[a] == 'R':
            reverse_state = not reverse_state
        elif p[a] == 'D':
            if nums_lst:
                if reverse_state:
                    nums_lst.pop()
                else:
                    nums_lst.popleft()
            else:
                print('error')
                return
        
    if reverse_state:
        nums_lst.reverse()
    return print('[' + ','.join(map(str, nums_lst)) + ']')

   

import sys, ast
from collections import deque
# sys.stdin = open("input.txt")

T = int(sys.stdin.readline()) #테케
for _ in range(T):   
    p = sys.stdin.readline() # 함수
    n = int(sys.stdin.readline()) # 배열 안 수의 개수
    nums = ast.literal_eval(sys.stdin.readline()) # 배열
    nums_lst = deque(nums)
    cal()

