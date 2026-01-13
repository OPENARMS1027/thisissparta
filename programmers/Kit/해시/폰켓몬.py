# 최대한 많은 종류의 포켓몬을 포함해 N/2마리 선택
# 포켓몬 종류 번호의 최대 개수 반환 

# 물리적인 한계의 개수를 잘 생각해서 풀어보자
# 문제에서 고르는 개수가 정해져있고, 최대 종의 개수도 정해져있음. 둘다 만족해야 하지 않을까 ?
def solution(nums):
    answer = min(len(nums)/2,len(set(nums)))
    return answer