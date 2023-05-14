a=int(input())
b=int(input())
c=int(input())
d=list(str(a*b*c))

for i in range(10):
    answer=0
    for j in range(len(d)):
        if str(d[j])==str(i):
            answer+=1
    print(answer)
