N = int(input())
nums = set(map(int,input().split()))
M = int(input())
check_nums = list(map(int,input().split()))

for k in check_nums:
    if k in nums:
        print(1)
    else:
        print(0)

'''
시간 복잡도
- in의 경우 리스트에서는 반복만큼 시간복잡도가 걸림
- set를 사용했을 때 in을 쓰면 시간복잡도는 평균 0(1)
'''

