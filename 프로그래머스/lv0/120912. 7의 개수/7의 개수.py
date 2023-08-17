def solution(array):
    answer = 0
    for i in array:
        a=list(str(i))
        for j in range(len(a)):
            if a[j]=="7":
                answer+=1
    return answer