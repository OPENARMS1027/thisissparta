def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    for h in range(len(citations)):
        if citations[h] >= h + 1:
            answer = h + 1
    print(answer)        
    return answer