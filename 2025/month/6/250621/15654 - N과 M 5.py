import sys
# sys.stdin = open("input.txt")

def backtracking(start,nums_set):
    
    if len(nums_set) == M:
        print(*nums_set)
        return 
    
    for i in range(N):
        number = nums[i]

        if nums[i] not in nums_set:
            nums_set.append(number)
            backtracking(0,nums_set)
            nums_set.pop()

N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
nums_set = []
backtracking(0,nums_set)  