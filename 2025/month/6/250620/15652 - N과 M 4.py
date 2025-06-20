import sys
# sys.stdin = open("input.txt")

def backtracking(start):
    if len(nums) == M:
        print(" ".join(map(str,nums)))
        return
    for num in range(start,N+1):
        nums.append(num)
        backtracking(num)
        nums.pop()

N,M = map(int,sys.stdin.readline().split())
nums = []
backtracking(1)

