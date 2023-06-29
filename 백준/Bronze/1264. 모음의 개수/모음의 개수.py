answer=0
while True:
    a=input()
    if a=="#":
        break
    else:
        b=list(a)
        for i in range(len(a)):
            if b[i]=="a" or b[i]=="e" or b[i]=="i" or b[i]=="o" or b[i]=="u" or b[i]=="A" or b[i]=="E" or b[i]=="I" or b[i]=="O" or b[i]=="U":
                answer+=1
        print(answer)
        answer=0

