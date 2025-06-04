import sys
N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,input().split()))
sum_lst = [0]

for num in nums:
    sum_lst.append(sum_lst[-1]+num)

for _ in range(M):
    total = 0
    start, end = map(int,sys.stdin.readline().split())
    answer = sum_lst[end]-sum_lst[start-1]
    print(answer)
    


