def solution(myString):
    answer = []
    a = []
    for i in range(len(myString)):
        if myString[i]=="x":
            a.append(i)
    answer.append(a[0])
    for i in range(1,len(a)):
        answer.append(a[i]-a[i-1]-1)
    answer.append(len(myString)-a[-1]-1)
    return answer
print(solution("oxooxoxxox"))
