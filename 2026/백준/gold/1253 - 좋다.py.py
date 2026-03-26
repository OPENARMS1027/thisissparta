import sys
# sys.stdin = open("input.txt")

N = int(input())
nums = list(map(int,input().split()))
nums.sort()
count = 0

for a in range(N):
    num = nums[a]
    left = 0
    right = N-1

    while left < right:
        cur = nums[left] + nums[right]
        if cur > num:
            right -= 1
        
        elif cur < num:
            left += 1

        elif cur == num:
            if left == a:
                left += 1
            elif right == a:
                right -= 1

            else:
                count += 1            
                break
    

print(count)
