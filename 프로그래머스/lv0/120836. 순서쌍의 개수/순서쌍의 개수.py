def solution(n):
    k=[]
    for i in range(1,n):
        if n%i==0:
            k.append(i)
    answer = len(k)
    return answer+1