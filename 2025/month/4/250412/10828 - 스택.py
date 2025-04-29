from collections import deque
import sys

N =int(sys.stdin.readline())
q = deque()
for i in range(N):
    input_value = sys.stdin.readline().split()
    command = input_value[0]

    if command == 'push':
        num = input_value[1]
        q.append(num)

    elif command == 'pop':
        if q:
            num = q.pop()
            print(num)
        else:
            print(-1)

    elif command == 'size':
        print(len(q))

    elif command == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif command == 'top':
        if q:
            num = q[-1]
            print(num)
        else:
            print(-1)
