import math
def solution(n):
    answer = 0
    if n==1:
        return 0
    for i in range(2,n+1):
        sosu=0
        for j in range(2,int(i**(1/2))+1):
            if i%j==0:
                sosu+=1
                break
        if sosu==0:
            answer+=1
    return answer