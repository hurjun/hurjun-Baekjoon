N,X=map(int,input().split())
A=list(map(int, input().split()))
answer=[]
for i in range(len(A)):
    if A[i]<X:
        answer.append(str(A[i]))
    b=" ".join(answer)
print(b)
