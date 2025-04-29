K = int(input())
sqaure_info = [list(map(int,input().split())) for _ in range(6)]

max_wid = 0
max_height= 0
max_width_dir = 0
max_height_dir = 0

for i in range(6):
    dir, len = sqaure_info[i]
    if dir == 1 or dir ==2:
        if len > max_wid:
            max_wid = len
            max_width_dir = i

    elif dir == 3 or dir == 4:
        if len > max_height:
            max_height = len
            max_height_dir = i

small_square_wid = abs(sqaure_info[(max_width_dir-1)%6][1] - sqaure_info[(max_width_dir+1)%6][1])
small_square_height = abs(sqaure_info[(max_height_dir-1)%6][1] - sqaure_info[(max_height_dir+1)%6][1])
small_square_dimension = small_square_wid * small_square_height

answer_square_dimension = (max_height * max_wid -small_square_dimension) * K
print(answer_square_dimension)