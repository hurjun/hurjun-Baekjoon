def solution(s):
    answer=[]
    ns = s.split(" ")
    for i in ns:
        answer.append(i.lower().capitalize())
    return " ".join(answer)
    