def solution(n):
    a=list(str(n))
    b=0
    for i in range(len(a)):
        b+=int(a[i])
    answer = b
    return answer