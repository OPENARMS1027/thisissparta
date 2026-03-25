import sys
# sys.stdin = open("input.txt")

N, new, P = map(int,input().split())
if N == 0:
    print(1)
    exit()

nums = list(map(int,input().split()))
count = 1

if N >= P and nums[-1] >= new:
    print(-1)

else:
    for num in nums:
        if num > new:
            count += 1
        
        else:
            break
    
    print(count)
    
        
    
        
