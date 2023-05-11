def solution(my_string, alp):
    answer = ''
    a=[]
    for i in my_string:
        if i==alp:
            a.append(i.upper())
        else:
            a.append(i)
    answer=''.join(a)
    
    return answer