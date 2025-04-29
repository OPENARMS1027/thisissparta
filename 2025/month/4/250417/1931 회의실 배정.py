import sys
N = int(sys.stdin.readline())

time_table = []
for i in range(N):
    start,end = map(int,sys.stdin.readline().split())
    time_table.append((start,end))

time_table.sort()
time_table.sort(key = lambda x:x[1])
# print(time_table)


'''
그냥 끝나는 시간으로만 정렬 했을 경우 앞 시간이 빠른거랑 상관없이 입력 순서대로 저장
예를 들면
3
3 3
2 3
1 3
따라서 시작시간별 먼저 정렬 해주고
끝나는 시간별 정렬 
sort()먼저해주고 sort(key=lambda x:x[1]) 해줌으로서 시작시간이 정렬된 상태가 보장되며 끝 시간 기준으로 정렬
'''
#
cur = time_table[0][1]
count = 1
# 앞에 end랑 그 뒤에 start 비교
for i in range(1,len(time_table)):
    if cur <= time_table[i][0]:
        count += 1
        cur = time_table[i][1]

print(count)

