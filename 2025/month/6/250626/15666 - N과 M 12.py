import sys
# sys.stdin = open("input.txt")
def backtracking(start,nums):
    if len(nums) == M:
        print(*nums)
        return
    
    cur_num = -1
    for a in range(start,N):
        if cur_num != lst[a]:
            nums.append(lst[a])
            cur_num = lst[a]
            backtracking(a,nums)
            nums.pop()

N,M = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

nums = []
lst.sort()
backtracking(0,nums)
