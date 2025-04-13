N = int(input())

num_lst = []
count = 0
for _ in range(N):
    num = int(input())
    num_lst.append(num)

standard = num_lst[-1]


# 제일 큰거부터 맨뒤에거 전까지 비교
for i in range(N-2,-1,-1):
    if standard < num_lst[i]:
        count += 1
        standard = num_lst[i]


count += 1 # 보이는 자기자신까지 더해주기        
print(count)
