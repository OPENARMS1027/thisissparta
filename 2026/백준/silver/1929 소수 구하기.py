# import sys
# sys.stdin = open("input.txt")

M,N = map(int,input().split())
for num in range(M,N+1):
    is_Sosu = True

    if num < 2:
        continue

    for idx in range(2,int(num**0.5)+1):
        if num % idx == 0:
            is_Sosu = False
            break
    
    if is_Sosu == True:
        print(num)