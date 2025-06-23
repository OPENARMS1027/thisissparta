"""
가장 긴 증가하는 부분 수열(LIS) 풀기
각 위치 원소가 가지는 증가하는 수열의 길이를 저장하는 dp배열을 이용
반복문을 이용해서, 한 원소위치 전까지 이 원소보다 작은 것이 있다면
수열 존재하므로 계산해주는 방법.
계산값 중 각 원소의 최대값을 찾아준다.
"""
import sys
# sys.stdin = open("input.txt")
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
dp = [1] * (N+1)

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
