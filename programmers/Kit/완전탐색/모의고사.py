def solution(answers):
    answer = []
    cnt_a, cnt_b, cnt_c = 0,0,0
    a = [1,2,3,4,5] * (10000 // 5)
    b = [2,1,2,3,2,4,2,5] * (10000 // 8)
    c = [3,3,1,1,2,2,4,4,5,5] * (10000 // 10)

    idx = 0
    
    while idx < len(answers):
        if answers[idx] == a[idx]:
            cnt_a += 1
        if answers[idx] == b[idx]:
            cnt_b += 1
        if answers[idx] == c[idx]:
            cnt_c += 1
        idx += 1
    
    max_val = max(cnt_a,cnt_b,cnt_c)
    if max_val == cnt_a:
        answer.append(1)
    if max_val == cnt_b:
        answer.append(2)
    if max_val == cnt_c:
        answer.append(3)
        
            
    return answer


"""
** enumerate를 사용하는 경우도 생각해볼 수 있음(idx와 값을 같이 사용)
** 또한 반복되는 패턴이기 때문에 나머지를 인덱스로 활용해서도 가능 !!!!
for i, ans in enumerate(answers):
    if ans == pa[i % len(pa)]:
        cnt_a += 1
    if ans == pb[i % len(pb)]:
        cnt_b += 1
    if ans == pc[i % len(pc)]:
        cnt_c += 1
    
"""