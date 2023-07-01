a=[]
b=[]
answer=[]
for _ in range(3):
    c,d=map(int,input().split())
    a.append(c)
    b.append(d)

for i in range(3):
    if a.count(a[i])==1:
        a4=a[i]
    if b.count(b[i])==1:
        b4=b[i]
print(a4,b4)

