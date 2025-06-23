import sys
"""
중복된 수를 어떻게 사용해주지 않을 것인가 ? 
visited 배열, 인덱스로 접근해준 이유는 ?
현재 깊이에서의 방문 중복을 어떻게 없애주었고,
인덱스가 다른 중복된 수는 어떻게 넣어줬는가 ?
"""
# [1,7,9,9]
sys.stdin = open("input.txt")
def backtracking():
    if len(nums) == M:
        print(*nums)
        return
    
    cur_num = -1 
    for i in range(N):
        if not visited[i] and num_lst[i] is not cur_num:
            visited[i] = True
            nums.append(num_lst[i])

            cur_num = num_lst[i]

            backtracking()
            visited[i] = False
            nums.pop()




N,M = map(int,sys.stdin.readline().split())
num_lst = list(map(int,sys.stdin.readline().split()))
num_lst.sort()
visited = [False] * N
nums = []

backtracking()