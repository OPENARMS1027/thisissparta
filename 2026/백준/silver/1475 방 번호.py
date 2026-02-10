# import sys
# sys.stdin = open("input.txt")

cnt_arr = [0] * 10
N = input()

set_cnt = 0
for num in N:
    num = int(num)
    cnt_arr[num] += 1

    if num != 6 and num != 9:
        set_cnt = max(set_cnt,cnt_arr[num])


six_nine_cnt = 0
if (cnt_arr[6] + cnt_arr[9]) % 2 == 0:
    six_nine_cnt = (cnt_arr[6] + cnt_arr[9]) // 2
else:
    six_nine_cnt = (cnt_arr[6] + cnt_arr[9]) // 2 + 1

set_cnt = max(set_cnt,six_nine_cnt)
print(set_cnt)



