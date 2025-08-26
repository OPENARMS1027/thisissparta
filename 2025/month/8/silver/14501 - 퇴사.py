import sys

sys.stdin = open("input.txt", 'r')
N = int(sys.stdin.readline())
total_max_p = 0
emp_lst = []

for _ in range(N):
    t, p = map(int,sys.stdin.readline().split())
    emp_lst.append([t,p])

idx = 0
#  앞에거 밀면서 가기
while idx < N:
    
    total_p = 0
    count = idx 

    #  내부적으로 더하기
    while True:
        count += emp_lst[count][0]

        if count > N:
            break
        total_p += emp_lst[count][1]  

    if total_max_p < total_p:
        total_max_p = total_p

    idx += 1
     
print(total_max_p)
    
        