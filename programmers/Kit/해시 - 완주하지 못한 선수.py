from collections import Counter
def solution(participant, completion):
    remainer = Counter(participant) - Counter(completion)
    print(remainer)
    answer = ''
    return answer