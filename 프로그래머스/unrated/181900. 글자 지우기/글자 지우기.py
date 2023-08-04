def solution(my_string, indices):
    answer = ''
    my_string=list(my_string)
    indices.sort(reverse=True)
    for i in range(len(indices)):
        del my_string[indices[i]]
    answer=''.join(my_string)
    return answer