import sys
sys.stdin = open("input.txt")

alphabet = {}
word = input()

for alpha in word:
    if alpha in alphabet:
        alphabet[alpha] += 1
    else:
        alphabet[alpha] = 1

# 딕셔너리 max 사용가능한지, 딕셔너리로 만들면 시간복잡도 괜찮은지 ?

cur_max = alphabet[word[0]]
check = 0
for cur in alphabet:
    if alphabet[cur] > cur_max:
        cur_max = cur
        check = alphabet[cur]
    
    elif alphabet[cur] == cur_max:
        answer = '?'
        break

answer = cur_max.upper()
print(answer)