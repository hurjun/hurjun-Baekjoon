a=int(input())
result=0
b=0
c=1
for i in range(a):
    temp=c
    c=b+c
    b=temp
print(b)