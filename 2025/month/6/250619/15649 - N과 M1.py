import sys

def backtracking():
    if len(nums) == M:
        print(" ".join(map(str,nums)))
        return 
    
    for num in range(1,N+1):
        if num not in nums:
            nums.append(num)
            backtracking()
            nums.pop()
        

# sys.stdin = open("input.txt")
N,M = map(int,sys.stdin.readline().split())
nums = []
backtracking()
