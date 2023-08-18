def solution(t, p):
    answer = 0
    a=[]
    for i in range(len(t)-len(p)+1):
        a.append(t[i:i+len(p)])
    print(a)
    for i in a:
        if int(i)<=int(p):
            answer+=1
    return answer