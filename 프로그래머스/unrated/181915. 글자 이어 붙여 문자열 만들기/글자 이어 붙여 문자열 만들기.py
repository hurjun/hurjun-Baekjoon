def solution(my_string, index_list):
    a=[]
    for i in range(len(index_list)):
        a.append(my_string[index_list[i]])
    answer = "".join(a)
    return answer