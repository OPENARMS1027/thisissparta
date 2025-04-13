# 연속된 온도의 합이 최대가 되는 값 출력
N, K = map(int,input().split()) # 측정한 전체 날짜 N, 연속된 날짜의 수 K
temperature = list(map(int,input().split()))
max_temp = float('-inf')
sum_temp = 0
for i in range(K):
    sum_temp += temperature[i]
a = 0
b = K
max_temp = max(max_temp,sum_temp)
while b < N:
    sum_temp -= temperature[a]
    sum_temp += temperature[b]
    max_temp = max(max_temp,sum_temp)
    a += 1
    b += 1


print(max_temp)
