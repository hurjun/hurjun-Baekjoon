def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(len(score)//m):
        a=score[m*i:(i+1)*m]
        answer+=min(a)*m
    return answer