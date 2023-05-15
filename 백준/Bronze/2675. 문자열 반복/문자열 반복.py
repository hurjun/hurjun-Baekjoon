a=int(input())
for _ in range(a):
    b,c = input().split()
    c=list(c)
    for i in range(len(c)):
        c[i]=c[i]*int(b)

    print("".join(c))