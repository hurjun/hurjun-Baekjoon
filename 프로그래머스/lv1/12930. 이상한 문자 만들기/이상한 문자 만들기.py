def solution(s):
    answer = ''
    a=list(s.split(' '))
    print(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j%2==0:
                answer+=a[i][j].upper()
            else:
                answer+=a[i][j].lower()
        answer+=" "
    
    return answer[0:-1]