def solution(emergency):
    temp = sorted(emergency,reverse=True)
    print(temp)
    result=[]
    for i in range(len(emergency)):
        result.append(temp.index(emergency[i])+1)
    
    return result