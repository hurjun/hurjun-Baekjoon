def solution(s):
    a=list(s)
    if len(a)%2==0:
        b=len(a)//2
        return a[b-1]+a[b]
    else:
        return a[len(a)//2]
    