a=int(input())

b=0
if a%4==0:
    b=a/4
else:
    b=a//4+1
print("long "*int(b)+"int")