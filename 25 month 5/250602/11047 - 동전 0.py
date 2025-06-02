import sys
N,K = map(int,sys.stdin.readline().split())

num_lst = []
for a in range(N):
    num = int(sys.stdin.readline())
    num_lst.append(num)

num_lst.sort(reverse=True)
# print(num_lst)

idx = 0 
count = 0
while K != 0:
    if K >= num_lst[idx]:
        counting = K // num_lst[idx]
        K = K % num_lst[idx]
        count += counting
    idx += 1

print(count)