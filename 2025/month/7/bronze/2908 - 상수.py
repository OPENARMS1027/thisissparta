A,B = input().split()
rev_A =''
rev_B =''
for i in range(len(A)-1,-1,-1):
    rev_A +=A[i]
for i in range(len(B)-1,-1,-1):
    rev_B += B[i]

if rev_A > rev_B:
    print(rev_A)
else:
    print(rev_B)