from collections import deque
import sys

# sys.stdin.readline 은 함수라서 괄호()를 사용해서 호출해야 한다.
N = int(sys.stdin.readline().strip())
q = deque()

for _ in range(N):
    input_value = sys.stdin.readline().split()
    command = input_value[0]

    if command == 'push':
        num = int(input_value[1])
        q.append(num)
        
    elif command == 'pop':
        if q:
            pop_num = q.popleft()
            print(pop_num)
        else:
            print(-1)
    
    elif command == 'size':
        print(len(q))
        
    elif command == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif command == 'front':
        if q:
            pop_num = q[0]
            print(pop_num)
        else:
            print(-1)
    
    elif command == 'back':
        if q:
            pop_num = q[-1]
            print(pop_num)
        else:
            print(-1)
