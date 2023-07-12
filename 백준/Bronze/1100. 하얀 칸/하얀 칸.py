a=[]
for _ in range(8):
    b=list(map(str,list(input())))
    a.append(b)
answer=0
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            if a[i][j]=="F":
                answer+=1
print(answer)