def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        temp=[]
        for j in range(queries[i][0],queries[i][1]+1):
            if arr[j]>queries[i][2]:
                temp.append(arr[j])
        if temp==[]:
            answer.append(-1)
        else:
            answer.append(min(temp))
    return answer