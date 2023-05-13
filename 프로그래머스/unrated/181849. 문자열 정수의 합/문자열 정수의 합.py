def solution(num_str):
    answer = 0
    a=list(num_str)
    print(a)
    b=list(map(int,a))
    for i in range(len(b)):
        answer+=b[i]
    return answer