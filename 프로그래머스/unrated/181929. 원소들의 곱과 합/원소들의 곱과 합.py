def solution(num_list):
    a=1
    b=0
    for i in range(len(num_list)):
        a=a*num_list[i]
        b+=num_list[i]
    c=b**2
    if a>c:
        return 0
    else: 
        return 1
  