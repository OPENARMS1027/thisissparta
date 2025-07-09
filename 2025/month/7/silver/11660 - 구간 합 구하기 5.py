import sys
# sys.stdin = open("input.txt")

def get_sum(x1,y1,x2,y2):
    answer = prefix[x2][y2] + prefix[x1-1][y1-1] - prefix[x1-1][y2] -prefix[x2][y1-1]
    return answer


N,M = map(int,sys.stdin.readline().split())
nums = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
prefix = [[0] * (N+1) for _ in range(N+1)]
for r in range(1,N+1):
    for c in range(1,N+1):
        prefix[r][c] = nums[r-1][c-1] + prefix[r-1][c]+prefix[r][c-1]-prefix[r-1][c-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    answer = get_sum(x1,y1,x2,y2)
    print(answer)


"""
그냥 하면 시간 초과 떠서 dp 사용
누적합을 사용할건데 어떻게 누적합을 구해서 할당할 것인가 ?
--> 끝점을 기준으로 누적합을 계산 

막혔던 부분
1. 메모이제이션 배열을 어떻게 만들어서 값을 계산할건지 ?
-> 이거 좀 고민해보고 여러가지 직접 해보면서 알아가기
2. 메모이제이션을 사용해도 시간 초과가 떴음
-> 매번 해줄 필요 없는거 주의 필요
3. 메모이제이션 되어있는 값을 어떻게 사용해서 계산할것인지 ?
-> 이거 도 고민해보고 직접 해보면서 인덱스 찾아가기
"""
