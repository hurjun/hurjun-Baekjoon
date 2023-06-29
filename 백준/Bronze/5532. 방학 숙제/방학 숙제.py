import math
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=math.ceil(b/d)
g=math.ceil(c/e)
print(a-max(f,g))