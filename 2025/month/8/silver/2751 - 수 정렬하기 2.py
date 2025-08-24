import sys
N = int(sys.stdin.readline()) 
emp_lst = []
for _ in range(N):
    num = int(sys.stdin.readline())
    emp_lst.append(num)

emp_lst.sort()
print(*emp_lst,sep='\n')


### Counting Sort도 가능

N = int(sys.stdin.readline())
check = [0] * 2000001

for _ in range(N):
    check[int(input())+1000000] + 1

for i in range(2000001):
    if check[i]:
        