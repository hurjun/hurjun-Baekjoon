def solution(x):
    answer = True
    a=list(str(x))
    b=0
    for i in range(len(a)):
        b+=int(a[i])
    if x%b==0:
        answer=True
    elif x%b!=0:
        answer=False
    return answer