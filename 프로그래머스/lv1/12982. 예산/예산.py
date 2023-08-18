def solution(d, budget):
    answer = 0
    a=sorted(d)
    for i in range(len(d)):
        budget-=a[i]
        if budget<0:
            break
        else:
            answer+=1
    return answer