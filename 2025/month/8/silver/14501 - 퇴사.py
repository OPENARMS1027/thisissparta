import sys

# sys.stdin = open("input.txt", 'r')
N = int(sys.stdin.readline())

time = []
point = []
for _ in range(N):
    t,p = map(int,sys.stdin.readline().split())
    time.append(t)
    point.append(p)

dp = [0] * (N+1)

for last in range(N-1,-1,-1):
    if last + time[last] <= N:
        dp[last] = max(dp[last+1], point[last] + dp[last+time[last]])
    else:
        dp[last] = dp[last+1]
    
print(max(dp))