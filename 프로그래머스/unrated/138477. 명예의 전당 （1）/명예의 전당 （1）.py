def solution(k, score):
    answer = []
    temp=[]
    for i in range(len(score)):
        temp.append(score[i])
        temp.sort()
        if len(temp)>k:
            del temp[0]
        answer.append(min(temp))
    return answer