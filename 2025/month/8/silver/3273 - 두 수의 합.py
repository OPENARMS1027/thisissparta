import sys
# sys.stdin = open("input.txt",'r')
n = int(sys.stdin.readline())
num_lst = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())
cnt = 0
num_lst.sort()
left,right = 0,n-1
for _ in range(n):
    if left > right or left == right:
        break
    if num_lst[left] + num_lst[right] == x:
        cnt += 1
        left += 1
        right -= 1

    if num_lst[left] + num_lst[right] < x:
        left += 1
    
    elif num_lst[left] + num_lst[right] > x:
        right -= 1

# print(cnt)

