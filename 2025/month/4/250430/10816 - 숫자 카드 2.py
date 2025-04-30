import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
M = int(input())
have_nums = list(map(int,input().split()))

counting = {}
# 딕셔너리 이용해서 몇 개 있는지 확인
for i in nums:
    if i in counting:
        counting[i] += 1
    
    else:
        counting[i] = 1

for a in have_nums:
    if a in counting:
        print(counting[a], end=' ')
    
    else:
        print(0,end=' ')