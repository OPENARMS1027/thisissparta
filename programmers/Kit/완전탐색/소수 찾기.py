def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def solution(numbers):
    digits = list(numbers)          
    n = len(digits)
    used = [False] * n              
    candidates = set()              

    def dfs(cur):
        if cur:
            candidates.add(int(cur))

        for i in range(n):
            if not used[i]:
                used[i] = True
                dfs(cur + digits[i])
                used[i] = False

    dfs("")

    answer = 0
    for num in candidates:
        if is_prime(num):
            answer += 1

    return answer
