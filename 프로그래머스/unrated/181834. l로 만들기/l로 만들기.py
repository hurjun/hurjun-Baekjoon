def solution(myString):
    answer = ''
    a=list(myString)
    for i in range(len(a)):
        if ord(a[i])<=ord("l"):
            answer+="l"
        else:
            answer+=a[i]
    return answer