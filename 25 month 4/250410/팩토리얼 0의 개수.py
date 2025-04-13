N = int(input())
arr = []
a = 1
for i in range(1,N+1):
    a *= i

idx = -1
count = 0
while True:
    if str(a)[idx] == '0':
        count += 1
        idx -= 1

    else:
        print(count)
        break



