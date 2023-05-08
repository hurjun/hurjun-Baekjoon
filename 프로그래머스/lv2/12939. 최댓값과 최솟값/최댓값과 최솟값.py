def solution(s):
    a=s.split(" ")
    b=list(map(int,a))
    c=sorted(b)
    
    answer = str(c[0])+" "+str(c[-1])
    return answer