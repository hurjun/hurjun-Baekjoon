a=int(input())
init=a
i=0
while True:
    i+=1
    b=a//10
    c=a%10
    d=b+c
    a=c*10+(d%10)
    if a==init:
        print(i)
        break