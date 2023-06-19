def solution(myString, pat):
    answer = 0
    a=list(myString)
    b=""
    for i in range(len(a)):
        if a[i]=="A":
            b+="B"
        else:
            b+="A"
    if pat in b:
        answer=1
    return answer