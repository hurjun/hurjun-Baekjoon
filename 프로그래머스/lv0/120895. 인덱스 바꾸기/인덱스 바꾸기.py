def solution(my_string, num1, num2):
    answer = ''
    a=list(my_string)
    pr=a[num1]
    a[num1]=a[num2]
    a[num2]=pr
    b=''.join(a)
    return b