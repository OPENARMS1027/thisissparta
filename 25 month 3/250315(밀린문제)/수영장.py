def good_consumption(index,total):
    global min_price
    # 12달 다 체크하면 return
    if index >= 13:
        if min_price > total:
            min_price = total
        return
    # 현재 최저 가격을 넘는다면 그냥 return
    if total > min_price: 
        return
    
    # 1일권으로 다 사는 경우
    good_consumption(index+1, total + oneday*plan[index])
    # 1달권으로 다 사는 경우
    good_consumption(index+1, total + onemonth)
    # 3달권으로 다 사는 경우
    good_consumption(index+3, total + threemonth)
    # 1년권으로 다 사는 경우
    good_consumption(index+12, total + oneyear)
    
            

    
T = int(input())

for tc in range(1,1+T):
    # 1일 이용권[0], 1달 이용권[1], 3달 이용권[2], 1년 이용권[3]
    oneday, onemonth, threemonth, oneyear = map(int,input().split())
    plan = [0] + list(map(int,input().split())) # 문자형으로 받아줌
    
    
    min_price = float('inf') # 이용권 구매 경우의 최솟값
    good_consumption(1,0)

    print(f"#{tc} {min_price}")


    
    