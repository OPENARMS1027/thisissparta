# # 0부터 9까지의 10개 숫자 중 6개의 숫자를 입력 받은 후, 완전탐색을 적용하여 Baby-gin 여부를 검사하는 프로그램을 작성하시오
# # 실습 문제의 경우 실제 babygin 게임과 다르다.
# # 마지막에 확인하는 것이기 때문에 각각 재사용하지 않고 2세트가 나오면 baby-gin 완성
# # 앞에서부터 검사를 할텐데 런부터 검사하면 예시) 555678 의 경우 베이비진이 아니라고 판단하기 때문에
# # triple부터 검사해준다.
# # 위에서 말했듯이 프로그래맹 babygin의 경우 사용 처리를 해줘야 한다.
#
# nums = list(map(int,input().split()))
# count = [0] * 10
# for i in range(len(nums)):
#     count[nums[i]] += 1
#
# # 이렇게 카드가 몇개가 있는지 체크
#
# baby_gin = False
# baby_gin = 0
# answer = False
#
# for _ in range(2):
#     # count 배열 안에서 체크
#     # triple 검사
#     for i in range(10):
#         if count[i] >= 3:
#             baby_gin += 1
#             count[i] -= 3
#
#     # run 검사
#     for i in range(8):
#         # 연속되는 3개의 수가 다 존재한다면
#         if count[i] > 0 and count[i+1] > 0 and count[i+2] > 0:
#                 baby_gin += 1
#                 count[i] -= 1
#                 count[i+1] -= 1
#                 count[i+2] -= 1
#
#
# # triple이 2번이거나 run이 2번인 경우도 babygin인데 위 코드의 경우 한 번만 검사하니까 2번 검사
# if baby_gin == 2:
#     answer = True
#
# print(answer)
#
#
lst = [1,2,3,4,5]
print(*lst,end='')
