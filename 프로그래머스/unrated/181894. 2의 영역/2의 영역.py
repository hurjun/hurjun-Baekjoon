def solution(arr):
    if arr.count(2)==0:
        return [-1]
    answer = []
    start=0
    end=len(arr)
    for i in range(len(arr)):
        if arr[i]==2:
            start=i
            break
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==2:
            end=i
            break

    return arr[start:end+1]
    