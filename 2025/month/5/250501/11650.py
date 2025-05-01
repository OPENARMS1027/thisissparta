N = int(input())
nums = []
for _ in range(N):
    x,y = map(int,input().split())
    nums.append((x,y))


nums.sort(key = lambda x: x[1])
nums.sort()
for i in range(N):
    print(*nums[i])