# A->B로 만드는 연산의 최솟값에 1을 더한 값 출력
# 만들 수 없는 경우 -1을 출력
"""
1. 안될 때 return값을 while문 안쪽에 둬도 되는가 ?
    - 크기를 넘었을 때, 넘지않았을 때 어느 것을 기준으로 삼음 ?
2. bfs 사용 이유 ?, 그냥 while문 쓰면 ?
3. 
"""
import sys
from collections import deque
# sys.stdin = open("input.txt")

def bfs(num,count):
    q = deque()
    q.append((num,count))

    while q:
        cur, count = q.popleft()

        if cur == B:
            return count+1
        
        next1 = cur * 2
        next2 = cur*10 +1

        if next1 <= B:
            q.append((next1,count+1))
        if next2 <= B:
            q.append((next2,count+1))
            
    # 딱 맞는 값이 나오지 않아서 반복문이 끝났을 때
    return - 1

A,B = map(int,sys.stdin.readline().split())
answer = bfs(A,0)
print(answer)
