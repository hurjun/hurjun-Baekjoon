def solution(n):
    answer = 1
    i=1
    while n>=answer:
        answer+=answer*i
        i+=1    
    return i-1