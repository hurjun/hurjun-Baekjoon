def solution(my_string, s, e):
    answer = ''
    a=list(my_string[s:e+1])
    a.reverse()
    b=''.join(a)
    return my_string[0:s]+b+my_string[e+1:]