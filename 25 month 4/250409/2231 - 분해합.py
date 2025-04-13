N = int(input())

answer = 0
for i in range(1,1000001):
    hap = 0
    for a in range(len(str(i))):
        hap += int(str(i)[a])
    if N == i + hap:
       answer = i
       break

print(answer)