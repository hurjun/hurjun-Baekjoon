def solution(n):
    answer = []
    if n%2==0:
        a=n//2
    else:
        a=n//2+1
    for i in range(a):
        answer.append(i*2+1)
    return answer