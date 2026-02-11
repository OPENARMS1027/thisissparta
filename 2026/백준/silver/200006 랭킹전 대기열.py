# import sys
# sys.stdin = open("input.txt")

p,m = map(int,input().split())

rooms = []
for _ in range(p):
    l,n = input().split()
    l = int(l)
    if rooms:
        for room in rooms:
            if len(room) >= m:
                continue
            if (room[0][0]-10) <= l <= (room[0][0]+10):
                room.append((l,n))
                break
        else:      
            rooms.append([(l,n)])

    else:
        rooms.append([(l,n)])

for room in rooms:
    room.sort(key=lambda x:x[1])
    if len(room) == m:
        print('Started!')
    
    else:
        print('Waiting!')
        
    for per in room:
        print(*per)