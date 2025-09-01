import heapq

def solve(tree):
    max_h = max(tree)
    diffs = [max_h - h for h in tree if h != max_h]

    ones = 0
    twos = 0
    for d in diffs:
        twos += d // 2
        ones += d % 2

    # greedy 조정
    while twos - ones > 1:
        twos -= 1
        ones += 2

    if twos >= ones:
        return twos * 2
    else:
        return ones * 2 - 1

T = int(input())
for _ in range(T):
    N = int(input())
    tree = list(map(int, input().split()))
    print(solve(tree))
