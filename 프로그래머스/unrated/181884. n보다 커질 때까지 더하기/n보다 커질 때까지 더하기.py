def solution(numbers, n):
    a=numbers[0]
    i=0
    while a<=n:
        i+=1
        a+=numbers[i]
        
    answer = a
    return answer