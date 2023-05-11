def solution(start, end):
    answer = []
    if start==end:
        return answer.append(start)
    else:
        for i in range(start,end+1,1):
            answer.append(i)
    
    return answer