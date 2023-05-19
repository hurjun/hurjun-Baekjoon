def solution(rsp):
    answer = ''
    a=list(rsp)
    for i in range(len(a)):
        if a[i]=="2":
            answer+="0"
        elif a[i]=="5":
            answer+="2"
        else:
            answer+="5"
    return answer