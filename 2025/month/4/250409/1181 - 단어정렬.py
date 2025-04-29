N = int(input())
arr =[]
for i in range(N):
    word = input()
    arr.append(word)

arr = list(set(arr))

arr.sort()
arr.sort(key=len)



# sort는 기본적으로 정수형은 오름차순, 문자는 알파벳 순
# key값을 준다면 오직 그 key값 기준으로만 정렬
# 여러기준으로 정렬하고 싶을 때 ?
# arr.sort(key=lambda x: (len(x),x)) 길이순 -> 길이 같으면 사전순

# for i in range(N-1,-1,-1):
#     for a in range(i):
#         # 작은거 맨 뒤로 보내기
#         if len(arr[a]) > len(arr[a+1]):
#             arr[a],arr[a+1] =arr[a+1],arr[a]
#
# arr.sort(key=)
# print(arr)
for w in arr:
    print(w)
