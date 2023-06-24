def solution(age):
    answer = ''
    a=str(age)
    b=list(a)
    for i in range(len(b)):
        if b[i]=="0":
            answer+="a"
        elif b[i]=="1":
            answer+="b"
        elif b[i]=="2":
            answer+="c"
        elif b[i]=="3":
            answer+="d"
        elif b[i]=="4":
            answer+="e"
        elif b[i]=="5":
            answer+="f"
        elif b[i]=="6":
            answer+="g"
        elif b[i]=="7":
            answer+="h"
        elif b[i]=="8":
            answer+="i"
        elif b[i]=="9":
            answer+="j"
    return answer