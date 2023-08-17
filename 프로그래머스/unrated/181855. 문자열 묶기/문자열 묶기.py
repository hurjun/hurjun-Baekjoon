def solution(strArr):
    answer = 0
    arr=[]
    for i in strArr:
        arr.append(len(i))
    tmp=[]
    for i in set(arr):
        tmp.append(arr.count(i))
        
    return max(tmp)