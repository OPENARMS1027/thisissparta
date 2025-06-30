# 도시의 치킨거리 = 모든 집의 치킨 거리의 합
# 최대 치킨집 개수 M개
# 최소가 되는 도시의 치킨 거리 구하기
# 0 , 1 - 집, 2 - 치킨집
import sys
# sys.stdin = open("input.txt")


def lets_chicken(sr,sc):
    len = float("inf")
    for r in range(N):
        for c in range(N):
            if city[r][c] == 2:
                len = min(len,abs(sr-r)+abs(sc-c))
    
    return len

N,M = map(int,sys.stdin.readline().split())
city = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

total = 0
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            answer = lets_chicken(r,c)
            total += answer

print(total)