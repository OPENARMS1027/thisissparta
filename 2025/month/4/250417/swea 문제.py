T = int(input())
for tc in range(1,1+T):
    N,M_1,M_2 = map(int,input().split()) # 종류 개수
    weight = list(map(int,input().split()))
    weight.sort()

    a = []
    b = []

    same_idx = 1
    idx = -1

    while True:
        if len(a) < M_1:
            a.append(weight[idx]*same_idx)
            idx -= 1
        if len(b) < M_2:
            b.append(weight[idx]*same_idx)
            idx -= 1
        same_idx += 1

        if abs(idx) > N:
            break
    answer = sum(a) + sum(b)
    print(f"#{tc} {answer}")





