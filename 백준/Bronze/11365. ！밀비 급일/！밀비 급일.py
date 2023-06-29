
while True:
    a=input()
    if a=="END":
        break
    else:
        b=list(a)
        b.reverse()
        d=''.join(b)
        print(d)

