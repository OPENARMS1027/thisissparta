import sys
from collections import deque

def find_value(idx,cur,operator):
    global max_val,min_val
    if idx == N:
        max_val = max(max_val,cur)
        min_val = min(min_val,cur)
        return
    
    for i, op in enumerate(['+','-','*','/']):
        if operator[i] > 0:
            operator[i] -= 1

            if op == '+':
                find_value(idx+1,cur+nums[idx],operator)
            elif op == '-':
                find_value(idx+1,cur-nums[idx],operator)
            elif op == '*':
                find_value(idx+1,cur*nums[idx],operator)
            elif op == '/':
                if cur < 0:
                    find_value(idx+1,-(abs(cur) // nums[idx]),operator)
                else:
                    find_value(idx+1, cur//nums[idx],operator)
    
            operator[i] += 1


# sys.stdin = open('input.txt','r')
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

#  ++ -- xx // 
operator = list(map(int,sys.stdin.readline().split()))
max_val = -1000000000
min_val = 1000000000
find_value(1,nums[0],operator)

print(max_val)
print(min_val)