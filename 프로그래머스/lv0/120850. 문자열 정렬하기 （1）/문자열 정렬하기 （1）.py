def solution(my_string):
    answer = []
    a=list(my_string)

    for i in range(len(a)):
        if a[i].isdigit()==1:
            answer.append(int(a[i]))

    answer.sort()
    return answer