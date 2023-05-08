def solution(s):
    
    a=list(s.lower())
    b=0
    c=0
    for i in range(len(a)):
        if a[i]=="p":
            b+=1
        elif a[i]=="y":
            c+=1
    if b==c:
        answer = True
    else:
        answer = False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer