
N = int(input())

emp_lst = []

# a단계 끝난 리스트 만들어주기
for i in range(1, N + 1):
    emp_lst.append(i)

# 재귀로 풀지 못 했음
# 같은 과정이 나온다면 일단 반복문을 우선으로 생각하기
# 이 문제의 경우 반복문에서 조건을 향하기 전까지 새로운 빈 리스트에 추가해주면서
# 계속해서 비교해간다. pop을 쓴다면 반복문내에서 index오류가 뜰 확률이 높다.
while True:
    lst = []
    for i in range(N):
        if i % 2 == 1:
            lst.append(emp_lst[i])

    emp_lst = lst
    N = len(emp_lst)
    if N == 1:
        break

print(lst[0])








