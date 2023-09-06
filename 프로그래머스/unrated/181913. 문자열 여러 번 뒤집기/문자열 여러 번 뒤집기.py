def solution(my_string, queries):
    for i in range(len(queries)):
        temp=my_string[queries[i][0]:queries[i][1]+1]
        temp=temp[::-1]
        my_string=my_string[0:queries[i][0]]+temp+my_string[queries[i][1]+1:]
    return my_string