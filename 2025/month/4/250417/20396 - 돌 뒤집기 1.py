import sys
sys.stdin = open('input.txt','r')
T = int(input())

for tc in range(1,1+T):
    N,K = map(int,input().split())

    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))

    s_idx = 0
    p_idx = 0
    answer = 0
    while s_idx < N:

        if p_idx >= K:
            answer = 1
            break

        if sample[s_idx] == passcode[p_idx]:
            p_idx += 1
        s_idx += 1

    print(answer)