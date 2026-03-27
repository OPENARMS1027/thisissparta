import sys
# sys.stdin = open("input.txt")

alphabet = {}
word = input().upper()

for alpha in word:
    if alpha in alphabet:
        alphabet[alpha] += 1
    else:
        alphabet[alpha] = 1

# 딕셔너리 max 사용가능한지, 딕셔너리로 만들면 시간복잡도 괜찮은지 ?

max_word = word[0]
check = 0
for cur_word in alphabet:
    if alphabet[cur_word] > check:
        answer = cur_word
        check = alphabet[cur_word]
    
    elif alphabet[cur_word] == check:
        answer = '?'


print(answer)



"""
1. 
훨씬 간단한 'Counter'라는 메서드가 있음
word = "AABBCCCA"
counts = Counter(word)
# 결과: Counter({'A': 3, 'C': 3, 'B': 2})
-> Counter에 문자열을 넣으면 내부적으로 딕셔너리 형태의 객체를 즉시 만들어준다.

2. 
most_common(n) 메서드
빈도수가 높은 순서대로 n개만 리스트로 반환
# 가장 많이 나온 상위 2개 추출
top_two = counts.most_common(2) 
# 결과: [('A', 3), ('C', 3)]  <-- (글자, 개수) 형태의 튜플 리스트

"""


