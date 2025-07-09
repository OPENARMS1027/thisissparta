import sys
sys.setrecursionlimit(3000)
def recur(a,b,memo,C):
    if b == 1:
        return a % C
    
    if b in memo:
        return memo[b]
    
    if b % 2 == 0:
        val = recur(a,b//2,memo,C)
        memo[b] = val * val 
        return memo[b] % C
        
    else:
        val = recur(a,(b-1)//2,memo,C)
        memo[b] = val * val * a 
        return memo[b] % C


A,B,C = map(int,sys.stdin.readline().split())
memo = {}
answer = recur(A,B,memo,C)
print(answer)

"""
파이썬에서 재귀호출 깊이 제한은 1000
스택의 한계를 넘어가면 'maximum recursion depth exceeded' 오류가 발생

방법 1.
sys.setrecursionlimit(3000) : 재귀 호출 깊이 제한

방법 2.
반복문 사용

반복 3. 
메모이제이션 사용


문제점
재귀만 사용 ?-> 시간 초과
여기에다가 메모이제이션(dp리스트 사용) ? -> 메모리 초과 dp리스트가 21억개 이상 원소여서
so how ? 필요한 값만 저장함(리스트 대신 dict쓰기 )

또 문제점 발생(시간 초과)
-> 수 자체가 크기 때문에 계산에 메모리 과다 사용.
문제의 조건인 % 해주는 것을 계산 중간에 해줘서 메모리 이득을 봐야 함
메모이제이션 해 줄 딕셔너리에 나머지를 넣어주는 형태

----------------------------


"""