from collections import deque

N, M =map(int,input().split())

a = set()
b = set()
for _ in range(N):
    see = input()
    a.add(see)

for _ in range(M):
    look = input()
    b.add(look)

c = sorted(a & b)

print(len(c))

for name in c:
    print(name)


'''
N, M = map(int, input().split())

a = set(input() for _ in range(N)) /// 제너레이터를 이용해서 값을 감싸면 자동으로 생성이 되는 것
b = set(input() for _ in range(M)) ///

# 교집합 찾기
c = sorted(a & b)  /// sorted는 '정렬된 리스트'를 반환해준다

print(len(c))
for name in c:
    print(name)
'''