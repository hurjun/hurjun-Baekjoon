a=int(input())
b=list(map(int,input().split()))
sosu=0
for i in range(a):
    error=0
    for j in range(2,b[i]):
        if b[i]%j==0:
            error+=1
    if error==0 and b[i]!=1:
        sosu+=1
print(sosu)
