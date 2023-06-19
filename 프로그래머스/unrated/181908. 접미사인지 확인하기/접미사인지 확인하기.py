def solution(my_string, is_suffix):
    
    answer = 0
    a=list(my_string)
    b=list(is_suffix)
    for i in range(len(a)):
        if a==b:
            answer=1
        else:
            a.remove(a[0])
    return answer