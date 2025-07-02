import sys
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**9)

def find_lcs(i,j):
    if i == len(fir) or j == len(sec):
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if fir[i] == sec[j]:
        dp[i][j] =  1 + find_lcs(i+1, j+1)

    else:
        dp[i][j] = max(find_lcs(i+1,j),find_lcs(i,j+1))
    
    return dp[i][j]

fir = sys.stdin.readline().strip()
sec = sys.stdin.readline().strip()
dp = [[-1] * len(sec) for _ in range(len(fir))]

answer = find_lcs(0,0)
print(answer)
"""
"두 가지 선택지 중, 더 나은 쪽을 고르는 것"
재귀 사용시 다음 계산에서 값이 반영되어야 할 필요가 있음.
따라서 다음 호출에서 값을 받아줘야 해서, return값에 값 지정


이 문제는 "값"을 이용해서 차곡 차곡 쌓아나가는 DP 문제
"""