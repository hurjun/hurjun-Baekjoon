def solution(myString):
    answer = ''
    a=list(myString)
    for i in range(len(a)):
        if a[i]=='a' or a[i]=="A":
            answer+='A'
        else:
            answer+=a[i].lower()
    return answer