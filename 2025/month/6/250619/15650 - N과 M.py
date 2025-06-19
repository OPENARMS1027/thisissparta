import sys
sys.stdin = open("input.txt")
def bfs(start):
    if len(nums) == M:
        print(' '.join(map(str,nums)))
        return
    
    for i in range(start,N+1):
        # if i not in nums:
        nums.append(i)
        bfs(i+1)    
        nums.pop()

N,M = map(int,sys.stdin.readline().split())
nums = []
bfs(1)