a=int(input())
for _ in range(a):
    b=list(input().strip())
    sum_score=0
    score=0
    for i in range(len(b)):
        if b[i]=="O":
            score+=1
            sum_score+=score
        else:
            score=0
    print(sum_score)