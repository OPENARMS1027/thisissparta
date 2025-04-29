T = int(input())
'''
먼저 두 로봇이 가야하는 지점을 각각 리스트로 만들어 준다.
주어진 테스트의 순서대로 로봇을 움직여야 하기 때문에 
로봇의 순서대로 가주기 위해 for문을 하나 더 돌려준다.
한 로봇의 차례대로 이동해야하는 만큼 count에 더해준 뒤
다른 로봇도 움직여주는데 먼저 움직여야 하는 로봇이 움직인 것 보다 많이 움직였다면
다른 로봇이 현재위치에서 가야하는 만큼에서 count를 빼주면 이 로봇 차례 때 가야할 count를 셀 수 있다.
'''
for tc in range(1,1+T):
    robot_botton = list(input().split())
    N = int(robot_botton.pop(0))
    position_B = []
    position_O = []
    # 가야하는 만큼 계산해주기 위해 값을 정수형으로 리스트에 넣어준다.
    for i in range(N):
        if robot_botton[2*i] == 'B':
            position_B.append(int(robot_botton[2*i+1]))
        if robot_botton[2*i] == 'O':
            position_O.append(int(robot_botton[2*i+1]))
    answer = 0
    # 1에서 시작
    cur_B = 1
    cur_O = 1
    
    
    
    # 리스트 순회하면서 체크해주기
    for i in range(N):
        count = 0

        if robot_botton[i*2] == 'B':
            # 눌러주는거까지 계산
            count += abs(int(robot_botton[i*2+1]) - cur_B) + 1
            cur_B = int(robot_botton[i*2+1])
            position_B.pop(0)
            # O 로봇의 위치를 계산
            if position_O:
                if count >= abs(position_O[0]-cur_O): # 둘의 차이를 절댓값 해준 것보다 count가 작다면
                    cur_O = position_O[0] # 카운트 수보다 덜 움직이기 때문에 그대로 가고가 하는 위치를 재할당
                else:
                    if position_O[0] > cur_O: # 만약 가야하는 위치가 더 크다면
                        cur_O += count # 카운트만큼 움직여주고
                    else: # 현재 위치가 더 크다면 돌아가야하기에
                        cur_O -= count #카운트만큼 빼준다
        elif robot_botton[i*2] == 'O':
            count += abs(int(robot_botton[i*2+1]) - cur_O) + 1
            cur_O = int(robot_botton[i*2+1])
            position_O.pop(0)
            if position_B:
                if count >= abs(position_B[0]-cur_B):
                    cur_B = position_B[0]
                else:
                    if position_B[0] > cur_B:
                        cur_B += count
                    else:
                        cur_B -= count
        answer += count          

    print(f"#{tc} {answer}")