def solution(clothes):
    fin = {}
    for name,cate in clothes:
        fin[cate] = fin.get(cate,0) + 1
    
    ans = 1
    for cate in fin:
        ans *= (fin[cate] + 1) 
    ans -= 1
    return ans