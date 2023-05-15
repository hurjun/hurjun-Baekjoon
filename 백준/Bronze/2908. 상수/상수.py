a,b=input().split()
c=list(a)
d=list(b)
c.reverse()
d.reverse()

e="".join(c)
f="".join(d)

if e>f:
    print(e)
else:
    print(f)
