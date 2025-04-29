from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    visited = [[0]* 6 for _ in range(12)] 
    visited[si][sj] = 1

    count = 1
    while q:
        r, c = q.popleft()

        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr <12 and 0<= nc <6 and visited[nr][nc] ==0:
                if ppuyo[nr][nc] == ppuyo[r][c]:
                    count +=1
                    visited[nr][nc] = 1
                    q.append((nr,nc))


    if count >= 4:           
        # 푸요된 곳 . 으로 바꿔주기
        for i in range(12):
            for j in range(6):
                if visited[i][j] == 1:
                    ppuyo[i][j] = ','

    return count 


def change(c):
    for r in range(11,1,-1):
        for k in range(r,-1,-1):
            if ppuyo[r][c] == '.':
                nr = r -1*k
                nc = c
                if 0<=nr<12 and ppuyo[nr][nc] != '.':
                    ppuyo[r][c], ppuyo[nr][nc] = ppuyo[nr][nc],ppuyo[r][c]



ppuyo = [list(map(str,input())) for _ in range(12)]

# R,G,B,P,Y
answer = 0
# 푸요 되어서 .으로 바꿔준 곳 다 밑으로 땡겨주기
for r in range(12): # 상하좌우 확인할 행
    ppuyo_count = 0
    for c in range(6): # 상하좌우 확인할 열
        if bfs(r,c) >= 4: # 푸요 되었을 때만 
            ppuyo_count += 1 # 푸요 카운트 올려주고
            change(c) # 아래로 땡겨주기
        else:
            answer = max(ppuyo_count,answer)
            ppuyo_count = 0
    answer = max(ppuyo_count, answer)

print(answer)
