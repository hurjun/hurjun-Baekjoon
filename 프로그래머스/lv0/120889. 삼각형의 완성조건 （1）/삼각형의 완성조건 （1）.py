def solution(sides):
    if sides[0]>=sides[1]+sides[2] or sides[1]>=sides[0]+sides[2] or sides[2]>=sides[0]+sides[1]:
        answer = 2
    else:
        answer = 1
    return answer