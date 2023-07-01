a=int(input())
for i in range(1,a+1):
    b=sum(map(int,str(i)))+i
    if b==a:
        print(i)
        break
    if i==a:
        print(0)