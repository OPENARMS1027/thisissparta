'''
DP는 작은 문제를 먼저 풀고 그 결과를 이용해서 큰 문제를 푸는 방식 !
따라서 초기값 설정이 중요함

'''


import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [0] * (11+1)
    dp[1] = 1 # (1)
    dp[2] = 2 # (1,1), (2)
    dp[3] = 4 # (1,1,1), (1,2), (2,1), (3)
    
    for i in range(4,N+1):
        # 마지막에 각 1,2,3 을 더했을 때 i가 생성되는 경우를 더하면 i를 생성하는 경우의 수를 모두 구할 수 있다.
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])
