def baby_gin(arr):
    # triplet
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] == arr[i+2]:
            return True
    # run
    arr = list(set(arr))
    for i in range(len(arr)-2):
        if arr[i] +1 == arr[i+1] and arr[i] + 2 == arr[i+2]:
            return True





T= int(input())
for tc in range(1,1+T):
    nums = list(map(int,input().split()))

    answer = 0 # 승부결과
    p1 = []
    p2 = []
    # 승자가 안 정해졌을 때

    for i in range(6):

        p1.append(nums[2*i])
        p2.append(nums[2*i+1])
        p1 = sorted(p1)
        p2 = sorted(p2)

        # 인덱스 2이상이면 3개 있음
        if i >= 2:
            if baby_gin(p1):
                answer = 1
                break
            if baby_gin(p2):
                answer = 2
                break

    print(f"#{tc} {answer}")








