a=[]
for i in range(4):
    a.append(int(input()))
f=sum(a)-min(a)
b=int(input())
c=int(input())
print(f+max(b,c))