import sys
M = int(sys.stdin.readline())
S = 0
for i in range(M):
    command = sys.stdin.readline().split()
    com = command[0]
    if len(command) > 1:
        num = int(command[1])
        
    if com == 'add':
        S = S | (1 << num-1)
            
    elif com == 'remove':
        S = S & ~(1<<num-1)
            
    elif com == 'check':
        if S & 1 << (num-1):
            print(1)
            
        else:
            print(0)
    elif com == 'toggle':
        S = S ^ (1<<num-1)
            
    elif com == 'all':
        S = (1<<21)-1
        
    elif com == 'empty':
        S = 0
        
'''
# 비트마스킹 이용
# 1. 추가 - i번째 비트만 1로 바꾸기  : or연산자 사용, 1을 빼준이유는 0부터이기 때문 
set = set | (1 << i-1)

# 2. 삭제 - i번째 비트만 0으로 바꾸기 : and 연산자 사용, !를 통해 i번째 비트만 0으로 바꿔줌
set = set & !(1 << i-1)

# 3. 토글 - i번째 비트 뒤집기 : xor연산자 이용해서 바꿔주기 -- xor 연산자 : 두 값이 다를때만 결과가 1, 같으면 0 
set = set ^ (1 << i-1)

# 4. 확인 - i번째 비트 1인지 0인지 : and 연산자로 1인지 확인
set = set & (1 << i-1)
'''