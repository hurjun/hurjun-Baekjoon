def solution(a, b):
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    day=["TUE","WED","THU","FRI","SAT","SUN","MON"]
    answer = 0
    for i in range(a-1):
        answer+=month[i]
    answer+=b-1
    return day[(answer%7)-4]
    return answer