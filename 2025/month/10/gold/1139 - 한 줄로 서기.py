import sys
# sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
memory = list(map(int,sys.stdin.readline().split()))
line = []

for a in range(N-1,-1,-1):
    line.insert(memory[a],a+1)

print(*line)

"""
줄을 찾아가는 게 아니라, "줄을 세워주는 방향"으로 접근
주어진 정보 자체가 "앞에 나보다 큰 사람이 몇명있냐"기 때문에
아직 줄에 서 있지 않은 더 작은 사람은 어차피 영향을 주지 않음
즉, 큰 사람들부터 줄을 세우면
이미 줄에 있는 사람들은 전부 "나보다 큰 사람"이 되기 때문에
조건을 그대로 적용할 수 있음
"""