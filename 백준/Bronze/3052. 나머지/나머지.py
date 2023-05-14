a=[]
for _ in range(10):
    b=int(input())%42
    a.append(b)
sum=0
for i in range(42):
    if a.count(i)!=0:
        sum+=1
print(sum)
