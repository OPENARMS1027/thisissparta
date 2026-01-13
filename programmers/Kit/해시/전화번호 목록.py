# 접두어인 경우가 있으면 false, 없으면 true 
# 중복된 전화번호는 없음 
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
    return answer