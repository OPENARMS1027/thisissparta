N = int(input())
nums = list(map(int,input().split()))

count = 0 
for a in nums:
    if a < 2:
        continue

    i = a-1
    while i >1:
        if a % i == 0:
            break
        i -= 1
    else:
        count += 1
print(count)