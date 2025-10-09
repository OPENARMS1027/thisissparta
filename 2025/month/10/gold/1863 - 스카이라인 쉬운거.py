import sys
# sys.stdin = open("input.txt")

"건물이 최소한 몇채인지 구하기"

n = int(sys.stdin.readline())
stack = []
min_buildings = 0

for a in range(n):
    x,y = map(int,sys.stdin.readline().split())
    
    while stack and stack[-1] > y:
        stack.pop()
        min_buildings += 1
    
    if  y > 0 and ( not stack or stack[-1] < y):
        stack.append(y)

if stack:
    min_buildings += len(stack)

print(min_buildings)


"""
스택을 이용하여 건물의 높이 변화에 따라서 로직을 구현해준다.
다음 높이 변화(건물 높이가 낮아지는 경우만)는 유지되던 건물이 
끝났음을 알 수 있음. 따라서 스택 top에 있는 건물보다 높이가 낮은
건물이 나온다면 스택에 있는 큰 건물을 이 건물보다 높지 않을 때 까지
계속해서 pop하고 count 해준다.

스택에 추가해주는 경우 0보다 크고(조건에 0이 있음)
앞선 과정에서 높은건 다 체크해주고 pop해줬기 때문에 높을 때만 고려해줌

마지막으로 높이가 내려가는 경우로 해줬기 때문에 높이가 높은 상태에서 끝나는 경우 대비
마지막에 스택에 있는 건물만큼 더해줘서
최소한의 건물을 구해준다.

"""