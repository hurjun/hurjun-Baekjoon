while True:
    A,B=map(int,input().split())
    if A>0 and B>0:
        if B/A>0 and B%A==0:
            print("factor")
        elif A/B>0 and A%B==0:
            print("multiple")
        else:
            print("neither")
    elif A==0 and B==0:
        break