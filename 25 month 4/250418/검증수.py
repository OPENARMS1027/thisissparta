lst = list(map(int,input().split()))

lst_sum = 0
for i in range(len(lst)):
    lst_sum += (lst[i] ** 2)

answer = lst_sum % 10

print(answer)
