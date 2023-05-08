def solution(n, control):
    a = list(control)
    for i in range(len(a)):
        if a[i]=="w":
            n+=1
        elif a[i]=="s":
            n-=1
        elif a[i]=="d":
            n+=10
        elif a[i]=="a":
            n-=10
    return n