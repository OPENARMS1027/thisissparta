def baby_gin(arr):
    result = False
    # triple
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] == arr[i+2]:
            result = True

    # run
    arr = list(set(arr))
    for i in range(len(arr)-2):
        if arr[i] + 1 == arr[i+1] and arr[i] + 2 == arr[i+2]:
            result = True

    return result

T = int(input())
for tc in range(1,1+T):
    nums = list(map(int,input().split()))
    p_1 = []
    p_2 = []
    winner = 0
    # 각 배열에 넣어주기
    for i in range(6):
        p_1.append(nums[2*i])
        p_2.append(nums[2*i+1])

        p_1.sort()
        p_2.sort()

        if i >= 2:
            if baby_gin(p_1):
                winner = 1
                break
            if baby_gin(p_2):
                winner = 2
                break

    print(f"#{tc} {winner}")