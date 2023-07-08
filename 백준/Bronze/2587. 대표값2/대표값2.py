A=[]
for i in range(5):
    A.append(int(input()))
print(sum(A)//5)
A=sorted(A)
print(A[2])