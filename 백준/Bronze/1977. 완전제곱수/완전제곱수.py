a=int(input())
b=int(input())
min=0
sum=0
for i in range(1,101):
    if a<=i**2 and b>=i**2:
        if min==0:
            min=i**2
        sum+=i**2
if sum==0:
    print(-1)
else:
    print(sum)
    print(min)
