def solution(my_string):
    answer = []
    a=list(my_string)
    for i in range(len(a)):
        answer.append(my_string[i:])
    answer.sort()
    return answer