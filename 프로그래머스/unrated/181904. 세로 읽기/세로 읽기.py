def solution(my_string, m, c):
    answer = ''
    array=[]
    for i in range(0,len(my_string),m):
        array.append(my_string[i:i+m])
    print(array)
    for i in range(0,len(array)):
        answer+=array[i][c-1]
    return answer