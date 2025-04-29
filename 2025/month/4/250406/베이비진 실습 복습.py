# 0부터 9까지의 10개 숫자 중 6개의 숫자를 입력 받은 후, 완전탐색을 적용하여 Baby-gin 여부를 검사하는 프로그램을 작성하시오
'''
4
1 2 4 7 8 3
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''

T = int(input())
for tc in range(1,1+T):
    nums = list(map(int,input().split()))
    count = [0] * 10
    baby_gin = False
    count_each = 0
    # 몇개 있는지 확인
    for i in range(len(nums)):
        num = nums[i]
        count[num] += 1

    for _ in range(2):

        # triple
        for i in range(10):
            if count[i] == 3:
                count_each += 1
                count[i] -= 3

        # run
        for i in range(8):
            if count[i] >0 and count[i+1] >0 and count[i+2] >0:
                count_each += 1
                count[i] -= 1
                count[i+1] -= 1
                count[i+2] -= 1

    if count_each == 2:
        baby_gin = True

    print(f"#{tc} {baby_gin}")













