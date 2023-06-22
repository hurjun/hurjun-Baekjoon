def solution(my_string):
    answer = ''
    a=list(my_string)
    for i in range(len(a)):
        if a[i].isupper()==1:
            answer+=a[i].lower()
        else:
            answer+=a[i].upper()
    return answer