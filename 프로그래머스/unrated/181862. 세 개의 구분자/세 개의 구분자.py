def solution(myStr):
    answer = ""
    for i in range(len(myStr)):

        if myStr[i]=="a" or myStr[i]=="b" or myStr[i]=="c":
            answer+=" "
        else:
            answer+=myStr[i]
    a=list(answer.split())
    if a==[]:
        a.append("EMPTY")
    return a