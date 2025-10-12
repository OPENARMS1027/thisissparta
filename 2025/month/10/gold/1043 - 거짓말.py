import sys
# sys.stdin = open("input.txt")

# 과장된 이야기를 할 수 있는 파티 개수의 최댓값 구하기
# 사람의 수 N, 파티의 수 M
N,M = map(int,sys.stdin.readline().split())
max_count = 0
# 아는 사람 수와 그 사람들의 번호
knew_people = list(map(int,sys.stdin.readline().split()))

knew_count = knew_people[0]
know_people_nums = knew_people[1:] if knew_count > 0 else []

party_people_data = []

# 각 파티마다 오는 사람의 수, 사람들의 번호 
for _ in range(M):
    parties = list(map(int,sys.stdin.readline().split()))
    
    party_num = parties[0]
    party_people_num = parties[1:]
    party_people_data.append(party_people_num)

changed = True
while changed:
    changed = False
    for party_people_num in party_people_data:
        flag = False
        for p in party_people_num:
            if p in know_people_nums:
                flag = True 
                break

        if flag:
            for p in party_people_num:
                if p not in know_people_nums:        
                    know_people_nums.append(p)
                    changed = True

for party_people_num in party_people_data:
    for p in party_people_num:
        if p in know_people_nums:
            break
    else:
        max_count += 1

print(max_count)

"""
주의점
1. 파티에는 순서가 없음
2. 입력을 잘 생각하자
3. 진실을 아는 사람이 한명이라도 있으면 다 진실만 듣게 됨


# 메모리 초과 발생!
36~37 번째 줄 그냥 append 해줬었는데
있는지 없는지 확인하고 append를 해주니 메모리 초과가 해결.

이유는 ?
조건에서 false가 안 바뀌기 때문 
"""
    



