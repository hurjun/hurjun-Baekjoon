def solution(arr):
    answer = []
    a=arr[0]
    for i in range(len(arr)):
        if a>arr[i]:
            a=arr[i]
    arr.remove(a)
    if len(arr)==0:
        answer = [-1]
    else:
        answer=arr
    return answer