def solution(myString, pat):
    start=0
    count=0
    while True:
        a=myString.find(pat,start)
        if a==-1:
            break
        count+=1
        start=a+1
    return count