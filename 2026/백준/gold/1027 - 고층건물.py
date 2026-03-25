import sys
# sys.stdin = open("input.txt")


N = int(input())
buildings = list(map(int,input().split()))


idx = 0
max_val = 0
while idx < N:
    right_max_val = 0
    left_max_val = 0
    max_slope = float("-inf")
    min_slope = float("inf")

    for a in range(idx+1,N):
        right_cur_slope = (buildings[a] - buildings[idx]) / (a - idx)
        if right_cur_slope > max_slope:
            right_max_val += 1
            max_slope = right_cur_slope
        
            

    back_idx = idx - 1
    for b in range(back_idx,-1,-1):
        left_cur_slope = (buildings[idx] - buildings[b]) / (idx - b)
        if left_cur_slope < min_slope:
            left_max_val += 1
            min_slope = left_cur_slope
        
    cur_val = left_max_val + right_max_val
    if cur_val > max_val:
        max_val = cur_val
    idx += 1  

print(max_val)
