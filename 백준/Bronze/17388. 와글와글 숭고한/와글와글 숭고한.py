a,b,c=map(int,input().split())
if a+b+c>=100:
    print("OK")
elif a+b+c<100:
    if min(a,b,c)==a:
        print("Soongsil")
    elif min(a,b,c)==b:
        print("Korea")
    else:
        print("Hanyang")
