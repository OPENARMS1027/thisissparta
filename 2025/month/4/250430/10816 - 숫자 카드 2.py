import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
M = int(input())
have_nums = list(map(int,input().split()))

check_nums = []
for i in range(M):
    count = 0
    for j in range(N):
        if have_nums[i] == nums[j]:
            count += 1
    check_nums.append(count)

print(*check_nums)
