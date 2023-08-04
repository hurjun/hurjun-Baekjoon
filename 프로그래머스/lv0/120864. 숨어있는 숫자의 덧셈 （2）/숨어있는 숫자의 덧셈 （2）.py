def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isalpha()==True:
            my_string=my_string.replace(i," ")
    a=list(my_string.split())
    return sum(map(int,a))