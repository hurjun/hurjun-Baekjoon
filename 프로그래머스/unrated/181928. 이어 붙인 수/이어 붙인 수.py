def solution(num_list):
    a=[]
    b=[]
    for i in range(len(num_list)):
        if num_list[i]%2==1:
            a.append(str(num_list[i]))
        elif num_list[i]%2==0:
            b.append(str(num_list[i]))
    c="".join(a)
    d="".join(b)
    answer=int(c)+int(d)
    return answer