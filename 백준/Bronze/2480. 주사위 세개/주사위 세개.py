a,b,c = map(int, input().split())
d=0
if a==b==c:
    d=10000+a*1000
elif a==b:
    d=1000+a*100
elif a==c:
    d=1000+a*100
elif b==c:
    d=1000+b*100
else:
    d=100*max(a,b,c)

print(d)