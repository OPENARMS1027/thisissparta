# import sys
# sys.stdin = open("input.txt")
money = int(input())
prices = list(map(int,input().split()))

jun = money
jun_stock = 0
song = money
song_stock = 0 

# 준현이 주식 개수 구하기
for price in prices:
    if jun >= price:
        jun_stock += (jun // price)
        jun = jun % price 

up_cnt = 0
down_cnt = 0
# 성민이 주식 개수 구하기
for idx in range(1,len(prices)):
    
    # 계속 오를 때 
    if prices[idx-1] < prices[idx]:
        down_cnt = 0
        up_cnt += 1
        if up_cnt == 3:
            song += prices[idx] * song_stock
            song_stock = 0
            up_cnt = 0 

    # 계속 내릴 때 
    elif prices[idx-1] > prices[idx]:
        up_cnt = 0
        down_cnt += 1
        if down_cnt == 3 and song >= prices[idx]:
            song_stock += (song // prices[idx])
            song = song % prices[idx]
            down_cnt = 0 

    elif prices[idx-1] == prices[idx]:
        up_cnt = 0
        down_cnt = 0 

jun = jun + jun_stock * prices[-1]
song = song + song_stock * prices[-1]

if jun > song:
    print('BNP')
elif song > jun:
    print('TIMING')
else:
    print('SAMESAME')
