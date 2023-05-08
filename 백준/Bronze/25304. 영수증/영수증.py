a=int(input())
b=int(input())
d=0
for i in range(b):
    b,c = map(int, input().split())
    d+=b*c
if a==d:
    print("Yes")
else:
    print("No")