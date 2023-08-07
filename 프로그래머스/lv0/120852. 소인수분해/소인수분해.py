def solution(n):
    answer = []
    a=[]
    b=2
    while b<=n:
        if n%b==0:
            answer.append(b)
            n=n//b
        elif n%b!=0:
            b+=1
    return list(dict.fromkeys(answer))
