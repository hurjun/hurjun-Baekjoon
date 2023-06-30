b=0
while b<=100:
    try:
        a=input()
        print(a)
        b+=1
    except EOFError:
        break