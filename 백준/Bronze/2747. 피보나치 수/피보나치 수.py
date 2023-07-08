a=0
b=1
put=int(input())
for i in range(put):
    c=a+b
    a=b
    b=c
print(a)