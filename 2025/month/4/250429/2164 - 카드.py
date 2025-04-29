from collections import deque

N =int(input())
nums = deque()
for i in range(N,0,-1):
    nums.append(i)


while len(nums) > 1:
    # 맨위 버리기
    nums.pop()
    # 그 다음 맨위거 맨 아래로 넣기
    a = nums.pop()
    nums.appendleft(a)

print(*nums)