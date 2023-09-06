def solution(s):
    answer = []
    for i in range(len(s)):
        temp=-1
        for j in range(0,i):
            if s[j]==s[i]:
                temp=i-j
        answer.append(temp)
    return answer